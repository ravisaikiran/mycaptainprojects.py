headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
import requests
import pandas
from bs4 import BeautifulSoup
url="https://www.oyorooms.com/hotels-in-bangalore/?page="
page_num=3
scraped_info_list=[]
for page in range(1,page_num+1):
    req=requests.get(url+str(page),headers=headers)
    soup=BeautifulSoup(req.content,'html.parser')
    all_hotels=soup.find_all('div',{'class':'hotelCardListing'})

    for hotel in all_hotels:
        hotel_dict={}
        hotel_dict['name']=hotel.find('h3',{'class':'listingHotelDescription__hotelName'}).text
        hotel_dict['address']=hotel.find('span',{'itemprop':'streetAddress'}).text
        hotel_dict['price']=hotel.find('span',{'class':'listingPrice__finalPrice'}).text
        try:
            hotel_dict['rating']=hotel.find('span',{'class':'hotelRating__ratingSummary'}).text
        except AttributeError:
            pass
        parent_amenities_element=hotel.find('div',{'class':'amenityWrapper'})
        amenity_list=[]
        for amenity in parent_amenities_element.find_all('div',{'class':'amenityWrapper__amenity'}):
            amenity_list.append(amenity.find('span',{'class':'d-body-sm'}).text.strip())
        hotel_dict['amenities']=', '.join(amenity_list[:-1])
        scraped_info_list.append(hotel_dict)
        #print(hotel_name,hotel_address,hotel_price,hotel_rating,amenity_list)
dataFrame=pandas.DataFrame(scraped_info_list)
dataFrame.to_csv('oyo.csv')

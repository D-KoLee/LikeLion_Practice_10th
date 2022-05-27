from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = "https://movie.naver.com/movie/bi/mi/basic.naver?code=182016"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
rank = 1

movie_title = soup.find('strong','blind')
movie_story = soup.find('p','con_tx')
print(movie_title.get_text())
print(movie_story.get_text())

search_rank_file = open("rankresult.txt","a")

# for result in results:
#     search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
#     print("리뷰",rank, " : ",result.get_text(),"\n")
#     rank += 1
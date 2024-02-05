# 1. 스킬서버예제(1)
from flask import Flask, request, jsonify
import pymysql
import re
import json
# Flask 인스턴스 생성
app = Flask(__name__)


# MariaDB 연결 설정

db = pymysql.connect(
   host="43.202.219.254",
    user="root",
    passwd="Rtgiu789!!od123sfnk+",
    db="ground",
    charset='utf8'
)

@app.route('/api/seyHello', methods=['GET'])
def hello():
    return "Hello Kakao-Chatbot!!"

# 공원 게시글 리스트
@app.route('/api/parkSeoul', methods=['POST'])
def parkSeoul():
    # JSON 데이터 받기
    body = request.get_json()

    # 응답 데이터 기본 구조
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "서울공원추천리스트"
                        },
                        "items": []
                    }
                }
            ]
            }
            }

    # 데이터베이스에서 정보 가져오기
    cursor = db.cursor()
    hash_tag_query = "SELECT hashTag FROM post"
    cursor.execute(hash_tag_query)
    hash_tag_data = cursor.fetchall()
    

    # 필터링된 해시태그가 있을 경우 추가 작업 수행
    title_query = """
                SELECT title, cntent, url_path, img_path
                FROM post 
                WHERE hashTag LIKE '%#서울%' AND hashTag LIKE '%#공원%'
                """

    cursor.execute(title_query)
    results = cursor.fetchall()
    
    # 결과가 있을 경우에 리스트에 추가하기
    for result in results:
        item = {
            "title":result[0],
            "description":result[1],
            "imageUrl":result[3],
            "link":{
                "web":result[2]
            }
        }
        response_body["template"]["outputs"][0]["listCard"]["items"].append(item)
    
    cursor.close()

    return jsonify(response_body)

@app.route('/api/parkGngi', methods=['POST'])
def parkGngi():
    # JSON 데이터 받기
    body = request.get_json()

    # 응답 데이터 기본 구조
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "경기공원추천리스트"
                        },
                        "items": []
                    }
                }
            ]
            }
            }

    # 데이터베이스에서 정보 가져오기
    cursor = db.cursor()
    hash_tag_query = "SELECT hashTag FROM post"
    cursor.execute(hash_tag_query)
    hash_tag_data = cursor.fetchall()
    

    # 필터링된 해시태그가 있을 경우 추가 작업 수행
    title_query = """
                SELECT title, cntent, url_path , img_path
                FROM post 
                WHERE hashTag LIKE '%#경기%' AND hashTag LIKE '%#공원%'
                """

    cursor.execute(title_query)
    results = cursor.fetchall()
    

    # 결과가 있을 경우에 리스트에 추가하기
    for result in results:
        item = {
            "title":result[0],
            "description":result[1],
            "imageUrl":result[3],
            "link":{
                "web":result[2]
            }
        }
        response_body["template"]["outputs"][0]["listCard"]["items"].append(item)
    
    cursor.close()

    return jsonify(response_body)

@app.route('/api/parkIcn', methods=['POST'])
def parkIcn():
    # JSON 데이터 받기
    body = request.get_json()

    # 응답 데이터 기본 구조
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "인천공원추천리스트"
                        },
                        "items": []
                    }
                }
            ]
            }
            }

    # 데이터베이스에서 정보 가져오기
    cursor = db.cursor()
    hash_tag_query = "SELECT hashTag FROM post"
    cursor.execute(hash_tag_query)
    hash_tag_data = cursor.fetchall()
    

    # 필터링된 해시태그가 있을 경우 추가 작업 수행
    title_query = """
                SELECT title , cntent, url_path, img_path
                FROM post 
                WHERE hashTag LIKE '%#인천%' AND hashTag LIKE '%#공원%'
                """

    cursor.execute(title_query)
    results = cursor.fetchall()
    

    # 결과가 있을 경우에 리스트에 추가하기
    for result in results:
        item = {
            "title":result[0],
            "description":result[1],
            "imageUrl":result[3],
            "link":{
                "web":result[2]
            }
        }
        response_body["template"]["outputs"][0]["listCard"]["items"].append(item)
    
    cursor.close()

    return jsonify(response_body)

@app.route('/api/parkBusan', methods=['POST'])
def parkBusan():
    # JSON 데이터 받기
    body = request.get_json()

    # 응답 데이터 기본 구조
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "부산공원추천리스트"
                        },
                        "items": []
                    }
                }
            ]
            }
            }

    # 데이터베이스에서 정보 가져오기
    cursor = db.cursor()
    hash_tag_query = "SELECT hashTag FROM post"
    cursor.execute(hash_tag_query)
    hash_tag_data = cursor.fetchall()
    

    # 필터링된 해시태그가 있을 경우 추가 작업 수행
    title_query = """
                SELECT title, cntent, url_path, img_path 
                FROM post 
                WHERE hashTag LIKE '%#부산%' AND hashTag LIKE '%#공원%'
                """

    cursor.execute(title_query)
    results = cursor.fetchall()
    

    # 결과가 있을 경우에 리스트에 추가하기
    for result in results:
        item = {
            "title":result[0],
            "description":result[1],
            "imageUrl":result[3],
            "link":{
                "web":result[2]
            }
        }
        response_body["template"]["outputs"][0]["listCard"]["items"].append(item)
    
    cursor.close()

    return jsonify(response_body)

@app.route('/api/parkGnju', methods=['POST'])
def parkGnju():
    # JSON 데이터 받기
    body = request.get_json()

    # 응답 데이터 기본 구조
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "광주공원추천리스트"
                        },
                        "items": []
                    }
                }
            ]
            }
            }

    # 데이터베이스에서 정보 가져오기
    cursor = db.cursor()
    hash_tag_query = "SELECT hashTag FROM post"
    cursor.execute(hash_tag_query)
    hash_tag_data = cursor.fetchall()
    

    # 필터링된 해시태그가 있을 경우 추가 작업 수행
    title_query = """
                SELECT title, cntent, url_path, img_path
                FROM post 
                WHERE hashTag LIKE '%#광주%' AND hashTag LIKE '%#공원%'
                """

    cursor.execute(title_query)
    results = cursor.fetchall()
    
    # 결과가 있을 경우에 리스트에 추가하기
    for result in results:
        item = {
            "title":result[0],
            "description":result[1],
            "imageUrl":result[3],
            "link":{
                "web":result[2]
            }
        }
        response_body["template"]["outputs"][0]["listCard"]["items"].append(item)
    
    cursor.close()

    return jsonify(response_body)

# 카페 게시글 리스트
@app.route('/api/cafeSeoul', methods=['POST'])
def cafeSeoul():
    # JSON 데이터 받기
    body = request.get_json()

    # 응답 데이터 기본 구조
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "서울카페추천리스트"
                        },
                        "items": []
                    }
                }
            ]
            }
            }

    # 데이터베이스에서 정보 가져오기
    cursor = db.cursor()
    hash_tag_query = "SELECT hashTag FROM post"
    cursor.execute(hash_tag_query)
    hash_tag_data = cursor.fetchall()
    

    # 필터링된 해시태그가 있을 경우 추가 작업 수행
    title_query = """
                SELECT title, cntent, url_path, img_path
                FROM post 
                WHERE hashTag LIKE '%#서울%' AND hashTag LIKE '%#카페%'
                """

    cursor.execute(title_query)
    results = cursor.fetchall()
    
    # 결과가 있을 경우에 리스트에 추가하기
    for result in results:
        item = {
            "title":result[0],
            "description":result[1],
            "imageUrl":result[3],
            "link":{
                "web":result[2]
            }
        }
        response_body["template"]["outputs"][0]["listCard"]["items"].append(item)
    
    cursor.close()

    return jsonify(response_body)

@app.route('/api/cafeGngi', methods=['POST'])
def cafeGngi():
    # JSON 데이터 받기
    body = request.get_json()

    # 응답 데이터 기본 구조
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "경기카페추천리스트"
                        },
                        "items": []
                    }
                }
            ]
            }
            }

    # 데이터베이스에서 정보 가져오기
    cursor = db.cursor()
    hash_tag_query = "SELECT hashTag FROM post"
    cursor.execute(hash_tag_query)
    hash_tag_data = cursor.fetchall()
    

    # 필터링된 해시태그가 있을 경우 추가 작업 수행
    title_query = """
                SELECT title, cntent, url_path, img_path
                FROM post 
                WHERE hashTag LIKE '%#경기%' AND hashTag LIKE '%#카페%'
                """

    cursor.execute(title_query)
    results = cursor.fetchall()
    
    # 결과가 있을 경우에 리스트에 추가하기
    for result in results:
        item = {
            "title":result[0],
            "description":result[1],
            "imageUrl":result[3],
            "link":{
                "web":result[2]
            }
        }
        response_body["template"]["outputs"][0]["listCard"]["items"].append(item)
    
    cursor.close()

    return jsonify(response_body)

@app.route('/api/cafeIcn', methods=['POST'])
def cafeIcn():
    # JSON 데이터 받기
    body = request.get_json()

    # 응답 데이터 기본 구조
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "인천카페추천리스트"
                        },
                        "items": []
                    }
                }
            ]
            }
            }

    # 데이터베이스에서 정보 가져오기
    cursor = db.cursor()
    hash_tag_query = "SELECT hashTag FROM post"
    cursor.execute(hash_tag_query)
    hash_tag_data = cursor.fetchall()
    

    # 필터링된 해시태그가 있을 경우 추가 작업 수행
    title_query = """
                SELECT title, cntent, url_path, img_path
                FROM post 
                WHERE hashTag LIKE '%#인천%' AND hashTag LIKE '%#카페%'
                """

    cursor.execute(title_query)
    results = cursor.fetchall()
    
    # 결과가 있을 경우에 리스트에 추가하기
    for result in results:
        item = {
            "title":result[0],
            "description":result[1],
            "imageUrl":result[3],
            "link":{
                "web":result[2]
            }
        }
        response_body["template"]["outputs"][0]["listCard"]["items"].append(item)
    
    cursor.close()

    return jsonify(response_body)

@app.route('/api/cafeBusan', methods=['POST'])
def cafeBusan():
    # JSON 데이터 받기
    body = request.get_json()

    # 응답 데이터 기본 구조
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "부산카페추천리스트"
                        },
                        "items": []
                    }
                }
            ]
            }
            }

    # 데이터베이스에서 정보 가져오기
    cursor = db.cursor()
    hash_tag_query = "SELECT hashTag FROM post"
    cursor.execute(hash_tag_query)
    hash_tag_data = cursor.fetchall()
    

    # 필터링된 해시태그가 있을 경우 추가 작업 수행
    title_query = """
                SELECT title, cntent, url_path, img_path
                FROM post 
                WHERE hashTag LIKE '%#부산%' AND hashTag LIKE '%#카페%'
                """

    cursor.execute(title_query)
    results = cursor.fetchall()
    
    # 결과가 있을 경우에 리스트에 추가하기
    for result in results:
        item = {
            "title":result[0],
            "description":result[1],
            "imageUrl":result[3],
            "link":{
                "web":result[2]
            }
        }
        response_body["template"]["outputs"][0]["listCard"]["items"].append(item)
    
    cursor.close()

    return jsonify(response_body)

@app.route('/api/cafeGnju', methods=['POST'])
def cafeGnju():
    # JSON 데이터 받기
    body = request.get_json()

    # 응답 데이터 기본 구조
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "광주카페추천리스트"
                        },
                        "items": []
                    }
                }
            ]
            }
            }

    # 데이터베이스에서 정보 가져오기
    cursor = db.cursor()
    hash_tag_query = "SELECT hashTag FROM post"
    cursor.execute(hash_tag_query)
    hash_tag_data = cursor.fetchall()
    

    # 필터링된 해시태그가 있을 경우 추가 작업 수행
    title_query = """
                SELECT title, cntent, url_path, img_path
                FROM post 
                WHERE hashTag LIKE '%#광주%' AND hashTag LIKE '%#카페%'
                """

    cursor.execute(title_query)
    results = cursor.fetchall()
    
    # 결과가 있을 경우에 리스트에 추가하기
    for result in results:
        item = {
            "title":result[0],
            "description":result[1],
            "imageUrl":result[3],
            "link":{
                "web":result[2]
            }
        }
        response_body["template"]["outputs"][0]["listCard"]["items"].append(item)
    
    cursor.close()

    return jsonify(response_body)

# 식당 게시글 리스트
@app.route('/api/DeSeoul', methods=['POST'])
def DeSeoul():
    # JSON 데이터 받기
    body = request.get_json()

    # 응답 데이터 기본 구조
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "서울맛집추천리스트"
                        },
                        "items": []
                    }
                }
            ]
            }
            }

    # 데이터베이스에서 정보 가져오기
    cursor = db.cursor()
    hash_tag_query = "SELECT hashTag FROM post"
    cursor.execute(hash_tag_query)
    hash_tag_data = cursor.fetchall()
    

    # 필터링된 해시태그가 있을 경우 추가 작업 수행
    title_query = """
                SELECT title, cntent, url_path, img_path
                FROM post 
                WHERE hashTag LIKE '%#서울%' AND hashTag LIKE '%#맛집%'
                """

    cursor.execute(title_query)
    results = cursor.fetchall()
    
    # 결과가 있을 경우에 리스트에 추가하기
    for result in results:
        item = {
            "title":result[0],
            "description":result[1],
            "imageUrl":result[3],
            "link":{
                "web":result[2]
            }
        }
        response_body["template"]["outputs"][0]["listCard"]["items"].append(item)
    
    cursor.close()

    return jsonify(response_body)

@app.route('/api/DeGngi', methods=['POST'])
def DeGngi():
    # JSON 데이터 받기
    body = request.get_json()

    # 응답 데이터 기본 구조
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "경기맛집추천리스트"
                        },
                        "items": []
                    }
                }
            ]
            }
            }

    # 데이터베이스에서 정보 가져오기
    cursor = db.cursor()
    hash_tag_query = "SELECT hashTag FROM post"
    cursor.execute(hash_tag_query)
    hash_tag_data = cursor.fetchall()
    

    # 필터링된 해시태그가 있을 경우 추가 작업 수행
    title_query = """
                SELECT title, cntent, url_path, img_path
                FROM post 
                WHERE hashTag LIKE '%#경기%' AND hashTag LIKE '%#맛집%'
                """

    cursor.execute(title_query)
    results = cursor.fetchall()
    
    # 결과가 있을 경우에 리스트에 추가하기
    for result in results:
        item = {
            "title":result[0],
            "description":result[1],
            "imageUrl":result[3],
            "link":{
                "web":result[2]
            }
        }
        response_body["template"]["outputs"][0]["listCard"]["items"].append(item)
    
    cursor.close()

    return jsonify(response_body)

@app.route('/api/DeIcn', methods=['POST'])
def DeIcn():
    # JSON 데이터 받기
    body = request.get_json()

    # 응답 데이터 기본 구조
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "인천맛집추천리스트"
                        },
                        "items": []
                    }
                }
            ]
            }
            }

    # 데이터베이스에서 정보 가져오기
    cursor = db.cursor()
    hash_tag_query = "SELECT hashTag FROM post"
    cursor.execute(hash_tag_query)
    hash_tag_data = cursor.fetchall()
    

    # 필터링된 해시태그가 있을 경우 추가 작업 수행
    title_query = """
                SELECT title, cntent, url_path, img_path
                FROM post 
                WHERE hashTag LIKE '%#인천%' AND hashTag LIKE '%#맛집%'
                """

    cursor.execute(title_query)
    results = cursor.fetchall()
    
    # 결과가 있을 경우에 리스트에 추가하기
    for result in results:
        item = {
            "title":result[0],
            "description":result[1],
            "imageUrl":result[3],
            "link":{
                "web":result[2]
            }
        }
        response_body["template"]["outputs"][0]["listCard"]["items"].append(item)
    
    cursor.close()

    return jsonify(response_body)

@app.route('/api/DeBusan', methods=['POST'])
def DeBusan():
    # JSON 데이터 받기
    body = request.get_json()

    # 응답 데이터 기본 구조
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "부산맛집추천리스트"
                        },
                        "items": []
                    }
                }
            ]
            }
            }

    # 데이터베이스에서 정보 가져오기
    cursor = db.cursor()
    hash_tag_query = "SELECT hashTag FROM post"
    cursor.execute(hash_tag_query)
    hash_tag_data = cursor.fetchall()
    

    # 필터링된 해시태그가 있을 경우 추가 작업 수행
    title_query = """
                SELECT title, cntent, url_path, img_path
                FROM post 
                WHERE hashTag LIKE '%#부산%' AND hashTag LIKE '%#맛집%'
                """

    cursor.execute(title_query)
    results = cursor.fetchall()
    
    # 결과가 있을 경우에 리스트에 추가하기
    for result in results:
        item = {
            "title":result[0],
            "description":result[1],
            "imageUrl":result[3],
            "link":{
                "web":result[2]
            }
        }
        response_body["template"]["outputs"][0]["listCard"]["items"].append(item)
    
    cursor.close()

    return jsonify(response_body)

@app.route('/api/DeGnju', methods=['POST'])
def DeGnju():
    # JSON 데이터 받기
    body = request.get_json()

    # 응답 데이터 기본 구조
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "광주맛집추천리스트"
                        },
                        "items": []
                    }
                }
            ]
            }
            }

    # 데이터베이스에서 정보 가져오기
    cursor = db.cursor()
    hash_tag_query = "SELECT hashTag FROM post"
    cursor.execute(hash_tag_query)
    hash_tag_data = cursor.fetchall()
    

    # 필터링된 해시태그가 있을 경우 추가 작업 수행
    title_query = """
                SELECT title, cntent, url_path, img_path
                FROM post 
                WHERE hashTag LIKE '%#광주%' AND hashTag LIKE '%#맛집%'
                """

    cursor.execute(title_query)
    results = cursor.fetchall()
    
    # 결과가 있을 경우에 리스트에 추가하기
    for result in results:
        item = {
            "title":result[0],
            "description":result[1],
            "imageUrl":result[3],
            "link":{
                "web":result[2]
            }
        }
        response_body["template"]["outputs"][0]["listCard"]["items"].append(item)
    
    cursor.close()

    return jsonify(response_body)

# 나잇대별 사용자 리스트
@app.route('/api/by70s', methods=['POST'])
def by70():
    # JSON 데이터 받기
    body = request.get_json()

    # 응답 데이터 기본 구조
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "프로필추천"
                        },
                        "items": []
                    }
                }
            ]
            }
            }

    # 데이터베이스에서 정보 가져오기
    cursor = db.cursor()
    user_list = "SELECT * FROM member, home"
    cursor.execute(user_list)
    user_list = cursor.fetchall()
    

    # 필터링된 정보에 생일이 있을 경우 추가 작업 수행
    title_query = """
                select mem.user_name, mem.text, mem.user_birth, mem.img_path, ho.mh_url from home ho , member mem
                where ho.user_id = mem.user_id and substr(user_birth, 1,2) between '70' and '74'
                """

    cursor.execute(title_query)
    results = cursor.fetchall()
    
    # 결과가 있을 경우에 리스트에 추가하기
    for result in results:
        item = {
            "title":result[0],
            "description":result[1],
            "imageUrl":result[3],
            "link":{
                "web":result[4]
            }
        }
        response_body["template"]["outputs"][0]["listCard"]["items"].append(item)
    
    cursor.close()

    return jsonify(response_body)

@app.route('/api/by75s', methods=['POST'])
def by75():
    # JSON 데이터 받기
    body = request.get_json()

    # 응답 데이터 기본 구조
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "프로필추천"
                        },
                        "items": []
                    }
                }
            ]
            }
            }

    # 데이터베이스에서 정보 가져오기
    cursor = db.cursor()
    user_list = "SELECT * FROM member, home"
    cursor.execute(user_list)
    user_list = cursor.fetchall()
    

    # 필터링된 정보에 생일이 있을 경우 추가 작업 수행
    title_query = """
                select mem.user_name, mem.text, mem.user_birth, mem.img_path, ho.mh_url from home ho , member mem
                where ho.user_id = mem.user_id and substr(user_birth, 1,2) between '75' and '79'
                """

    cursor.execute(title_query)
    results = cursor.fetchall()
    
    # 결과가 있을 경우에 리스트에 추가하기
    for result in results:
        item = {
            "title":result[0],
            "description":result[1],
            "imageUrl":result[3],
            "link":{
                "web":result[4]
            }
        }
        response_body["template"]["outputs"][0]["listCard"]["items"].append(item)
    
    cursor.close()

    return jsonify(response_body)

@app.route('/api/by80s', methods=['POST'])
def by80():
    # JSON 데이터 받기
    body = request.get_json()

    # 응답 데이터 기본 구조
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "프로필추천"
                        },
                        "items": []
                    }
                }
            ]
            }
            }

    # 데이터베이스에서 정보 가져오기
    cursor = db.cursor()
    user_list = "SELECT * FROM member, home"
    cursor.execute(user_list)
    user_list = cursor.fetchall()
    

    # 필터링된 정보에 생일이 있을 경우 추가 작업 수행
    title_query = """
                select mem.user_name, mem.text, mem.user_birth, mem.img_path, ho.mh_url from home ho , member mem
                where ho.user_id = mem.user_id and substr(user_birth, 1,2) between '80' and '84'
                """

    cursor.execute(title_query)
    results = cursor.fetchall()
    
    # 결과가 있을 경우에 리스트에 추가하기
    for result in results:
        item = {
            "title":result[0],
            "description":result[1],
            "imageUrl":result[3],
            "link":{
                "web":result[4]
            }
        }
        response_body["template"]["outputs"][0]["listCard"]["items"].append(item)
    
    cursor.close()

    return jsonify(response_body)

@app.route('/api/by85s', methods=['POST'])
def by85():
    # JSON 데이터 받기
    body = request.get_json()

    # 응답 데이터 기본 구조
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "프로필추천"
                        },
                        "items": []
                    }
                }
            ]
            }
            }

    # 데이터베이스에서 정보 가져오기
    cursor = db.cursor()
    user_list = "SELECT * FROM member, home"
    cursor.execute(user_list)
    user_list = cursor.fetchall()
    

    # 필터링된 정보에 생일이 있을 경우 추가 작업 수행
    title_query = """
                select mem.user_name, mem.text, mem.user_birth, mem.img_path, ho.mh_url from home ho , member mem
                where ho.user_id = mem.user_id and substr(user_birth, 1,2) between '85' and '89'
                """

    cursor.execute(title_query)
    results = cursor.fetchall()
    
    # 결과가 있을 경우에 리스트에 추가하기
    for result in results:
        item = {
            "title":result[0],
            "description":result[1],
            "imageUrl":result[3],
            "link":{
                "web":result[4]
            }
        }
        response_body["template"]["outputs"][0]["listCard"]["items"].append(item)
    
    cursor.close()

    return jsonify(response_body)

@app.route('/api/by90s', methods=['POST'])
def by90():
    # JSON 데이터 받기
    body = request.get_json()

    # 응답 데이터 기본 구조
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "프로필추천"
                        },
                        "items": []
                    }
                }
            ]
            }
            }

    # 데이터베이스에서 정보 가져오기
    cursor = db.cursor()
    user_list = "SELECT * FROM member, home"
    cursor.execute(user_list)
    user_list = cursor.fetchall()
    

    # 필터링된 정보에 생일이 있을 경우 추가 작업 수행
    title_query = """
                select mem.user_name, mem.text, mem.user_birth, mem.img_path, ho.mh_url from home ho , member mem
                where ho.user_id = mem.user_id and substr(user_birth, 1,2) between '90' and '94'
                """

    cursor.execute(title_query)
    results = cursor.fetchall()
    
    # 결과가 있을 경우에 리스트에 추가하기
    for result in results:
        item = {
            "title":result[0],
            "description":result[1],
            "imageUrl":result[3],
            "link":{
                "web":result[4]
            }
        }
        response_body["template"]["outputs"][0]["listCard"]["items"].append(item)
    
    cursor.close()

    return jsonify(response_body)

@app.route('/api/by95s', methods=['POST'])
def by95():
    # JSON 데이터 받기
    body = request.get_json()

    # 응답 데이터 기본 구조
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "프로필추천"
                        },
                        "items": []
                    }
                }
            ]
            }
            }

    # 데이터베이스에서 정보 가져오기
    cursor = db.cursor()
    user_list = "SELECT * FROM member, home"
    cursor.execute(user_list)
    user_list = cursor.fetchall()
    

    # 필터링된 정보에 생일이 있을 경우 추가 작업 수행
    title_query = """
                select mem.user_name, mem.text, mem.user_birth, mem.img_path, ho.mh_url from home ho , member mem
                where ho.user_id = mem.user_id and substr(user_birth, 1,2) between '95' and '99'
                """

    cursor.execute(title_query)
    results = cursor.fetchall()
    
    # 결과가 있을 경우에 리스트에 추가하기
    for result in results:
        item = {
            "title":result[0],
            "description":result[1],
            "imageUrl":result[3],
            "link":{
                "web":result[4]
            }
        }
        response_body["template"]["outputs"][0]["listCard"]["items"].append(item)
    
    cursor.close()

    return jsonify(response_body)

@app.route('/api/by00s', methods=['POST'])
def by00():
    # JSON 데이터 받기
    body = request.get_json()

    # 응답 데이터 기본 구조
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "프로필추천"
                        },
                        "items": []
                    }
                }
            ]
            }
            }

    # 데이터베이스에서 정보 가져오기
    cursor = db.cursor()
    user_list = "SELECT * FROM member, home"
    cursor.execute(user_list)
    user_list = cursor.fetchall()
    

    # 필터링된 정보에 생일이 있을 경우 추가 작업 수행
    title_query = """
                select mem.user_name, mem.text, mem.user_birth, mem.img_path, ho.mh_url from home ho , member mem
                where ho.user_id = mem.user_id and substr(user_birth, 1,2) between '00' and '04'
                """

    cursor.execute(title_query)
    results = cursor.fetchall()
    
    # 결과가 있을 경우에 리스트에 추가하기
    for result in results:
        item = {
            "title":result[0],
            "description":result[1],
            "imageUrl":result[3],
            "link":{
                "web":result[4]
            }
        }
        response_body["template"]["outputs"][0]["listCard"]["items"].append(item)
    
    cursor.close()

    return jsonify(response_body)

@app.route('/api/by05s', methods=['POST'])
def by05():
    # JSON 데이터 받기
    body = request.get_json()

    # 응답 데이터 기본 구조
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "프로필추천"
                        },
                        "items": []
                    }
                }
            ]
            }
            }

    # 데이터베이스에서 정보 가져오기
    cursor = db.cursor()
    user_list = "SELECT * FROM member, home"
    cursor.execute(user_list)
    user_list = cursor.fetchall()
    

    # 필터링된 정보에 생일이 있을 경우 추가 작업 수행
    title_query = """
                select mem.user_name, mem.text, mem.user_birth, mem.img_path, ho.mh_url from home ho , member mem
                where ho.user_id = mem.user_id and substr(user_birth, 1,2) between '05' and '09'
                """

    cursor.execute(title_query)
    results = cursor.fetchall()
    
    # 결과가 있을 경우에 리스트에 추가하기
    for result in results:
        item = {
            "title":result[0],
            "description":result[1],
            "imageUrl":result[3],
            "link":{
                "web":result[4]
            }
        }
        response_body["template"]["outputs"][0]["listCard"]["items"].append(item)
    
    cursor.close()

    return jsonify(response_body)

@app.route('/api/by10s', methods=['POST'])
def by10():
    # JSON 데이터 받기
    body = request.get_json()

    # 응답 데이터 기본 구조
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "프로필추천"
                        },
                        "items": []
                    }
                }
            ]
            }
            }

    # 데이터베이스에서 정보 가져오기
    cursor = db.cursor()
    user_list = "SELECT * FROM member, home"
    cursor.execute(user_list)
    user_list = cursor.fetchall()
    

    # 필터링된 정보에 생일이 있을 경우 추가 작업 수행
    title_query = """
                select mem.user_name, mem.text, mem.user_birth, mem.img_path, ho.mh_url from home ho , member mem
                where ho.user_id = mem.user_id and substr(user_birth, 1,2) between '10' and '14'
                """

    cursor.execute(title_query)
    results = cursor.fetchall()
    
    # 결과가 있을 경우에 리스트에 추가하기
    for result in results:
        item = {
            "title":result[0],
            "description":result[1],
            "imageUrl":result[3],
            "link":{
                "web":result[4]
            }
        }
        response_body["template"]["outputs"][0]["listCard"]["items"].append(item)
    
    cursor.close()

    return jsonify(response_body)

@app.route('/api/by15s', methods=['POST'])
def by15():
    # JSON 데이터 받기
    body = request.get_json()

    # 응답 데이터 기본 구조
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "프로필추천"
                        },
                        "items": []
                    }
                }
            ]
            }
            }

    # 데이터베이스에서 정보 가져오기
    cursor = db.cursor()
    user_list = "SELECT * FROM member, home"
    cursor.execute(user_list)
    user_list = cursor.fetchall()
    

    # 필터링된 정보에 생일이 있을 경우 추가 작업 수행
    title_query = """
                select mem.user_name, mem.text, mem.user_birth, mem.img_path, ho.mh_url from home ho , member mem
                where ho.user_id = mem.user_id and substr(user_birth, 1,2) between '14' and '20'
                """

    cursor.execute(title_query)
    results = cursor.fetchall()
    
    # 결과가 있을 경우에 리스트에 추가하기
    for result in results:
        item = {
            "title":result[0],
            "description":result[1],
            "imageUrl":result[3],
            "link":{
                "web":result[4]
            }
        }
        response_body["template"]["outputs"][0]["listCard"]["items"].append(item)
    
    cursor.close()

    return jsonify(response_body)

# 방문자가 제일 많은 미니홈페이지
@app.route('/api/mvhm', methods=['POST'])
def mvhm():
    # JSON 데이터 받기
    body = request.get_json()

    # 응답 데이터 기본 구조
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "방문자가 제일 많은 미니홈피"
                        },
                        "items": []
                    }
                }
            ]
            }
            }

    # 데이터베이스에서 정보 가져오기
    cursor = db.cursor()
    home_list = "SELECT * FROM member, home"
    cursor.execute(home_list)
    home_list = cursor.fetchall()
    

    # 필터링된 정보에 방문자수가 많은 홈페이지 5개 추가 작업 수행
    title_query = """
                SELECT mem.user_name, mem.img_path, ho.introduce , ho.total, ho.mh_url from home ho, member mem 
                where ho.user_id = mem.user_id order by total desc limit 5
                """

    cursor.execute(title_query)
    results = cursor.fetchall()
    
    # 결과가 있을 경우에 리스트에 추가하기
    for result in results:
        item = {
            "title":result[0],
            "description": f"방문자수: {result[3]}명",
            "imageUrl":result[1],
            "link":{
                "web":result[4]
            }
        }
        response_body["template"]["outputs"][0]["listCard"]["items"].append(item)
    
    cursor.close()

    return jsonify(response_body)

# 1) 카카오톡 텍스트형 응답
@app.route('/api/seyHello', methods=['POST'])
def sayHello():
    body = request.get_json()
#     print(body)

    responseBody = {
        "version" : "2.0",
        "template" : {
            "outputs":[
                {
                    "simpleText":{
                        "text": "안녕하세요? 그라운드 챗봇입니다 !!!"
                    }
                }
            ]
        }
    }
    
    return responseBody


           
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
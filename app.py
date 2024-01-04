# 1. 스킬서버예제(1)
from flask import Flask, request, jsonify
import pymysql
import re
import json
# Flask 인스턴스 생성
app = Flask(__name__)


# MariaDB 연결 설정

db = pymysql.connect(
    host="13.209.185.102",
    user="root",
    passwd="12345",
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
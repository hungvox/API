from flask import Flask, jsonify, request
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
import geopy.distance

# Cấu hình database
DATABASE_URI = "sqlite:///D:/TEST/mydatabase.db"

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Kết nối với database và tạo mô hình dữ liệu
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(80))
    password = Column(String(80))
    created_at = Column(DateTime)

class Island(Base):
    __tablename__ = "islands"

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    longitude = Column(Float)
    latitude = Column(Float)
    area = Column(Float)
    detected_time = Column(DateTime)

Base.metadata.create_all(engine)

# Lấy danh sách đảo
@app.route("/islands", methods=['GET'])
def get_islands():
    # Lấy vị trí người dùng từ request
    latitude = request.args.get("latitude")
    longitude = request.args.get("longitude")

    if latitude is None or longitude is None:
        return jsonify({"error": "Thiếu tham số vị trí"}), 400

    try:
        user_latitude = float(latitude)
        user_longitude = float(longitude)
        user_location = (user_latitude, user_longitude)  # Định nghĩa user_location ở đây
    except ValueError:
        return jsonify({"error": "Lỗi định dạng dữ liệu vị trí"}), 400

    # Truy vấn danh sách đảo
    islands = session.query(Island).all()

    # Tính toán khoảng cách cho mỗi đảo
    for island in islands:
        island_location = (island.latitude, island.longitude)
        distance = geopy.distance.geodesic(user_location, island_location).km
        island.distance = distance

    # Sắp xếp và trả về danh sách theo khoảng cách
    islands.sort(key=lambda island: island.distance)
    response = {
        "islands": [
            {
                "id": island.id,
                "name": island.name,
                "distance": island.distance,
            }
            for island in islands
        ]
    }

    return jsonify(response)

# Khởi động ứng dụng
if __name__ == "__main__":
    app.run(debug=True)

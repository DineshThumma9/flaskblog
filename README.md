# FlaskBlog
  FlaskBlog is a full-featured blogging web app built with **Flask**, styled using **Bootstrap**, and containerized with **Docker**.
  It includes full **authentication**, **CRUD for posts**, **profile image uploads**, and is live on **Render**.

  
## 🔧 Features
- **User Authentication**-Register,Login,Logout
- **Create,Edit,Delete Post**
- **Upload Profile Pic**
- **Bootstrap** for desgin
- **Dockerized** for deployement
- **Deployed on Render**

---

## 🚀 Tech Stack
 - **Framework**: Flask
 - **Templates**: Bootstrap
 - **Containerzation**: Docker
 - **Deploment**: Render

---

## ⚙️ Set Up

## 1.Clone App
 ```
git clone https://github.com/DineshThumma9/flaskblog.git
cd cuddly-waffle 
```

```
SECRET_KEY=your_secret_key
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
```
## 🌐 Live Demo
https://flaskblog-pumr.onrender.com/

## Docker
```
docker build -t flaskblog .
docker run -p 5000:5000 flaskblog
```

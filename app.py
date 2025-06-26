# from flask import Flask, request, render_template, redirect
# import psycopg2
# import psycopg2.extras

# app = Flask(__name__)

# def get_connection():
#     return psycopg2.connect(
#         dbname="localhost",
#         user="postgres",
#         password="newpassword",
#         host="localhost",
#         port="5432"
#     )

# @app.route("/", methods=["POST"])
# def upload_file():

#         file = request.files["file"]
#         if file:
#             filename = file.filename
#             filetype = file.content_type
#             filedata = file.read()

#             conn = get_connection()
#             cur = conn.cursor()
#             cur.execute("""
#                 INSERT INTO documents.files (filename, filetype, filedata)
#                 VALUES (%s, %s, %s)
#             """, (filename, filetype, psycopg2.Binary(filedata)))
#             conn.commit()
#             cur.close()
#             conn.close()

#             return "File uploaded successfully!"



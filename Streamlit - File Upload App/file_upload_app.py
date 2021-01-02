
import streamlit as st

# File Processing Pkgs
from PIL import Image
import pandas as pd
import docx2txt
# import textract
from PyPDF2 import PdfFileReader
import pdfplumber

PAGE_CONFIG = {"page_title":"FileUpload",
				"page_icon":":smiley:",
				"layout":"centered" }
st.set_page_config(**PAGE_CONFIG)


# Load Images
@st.cache
def load_image(image_file):
	img = Image.open(image_file)
	return img

def read_pdf(file):
	pdfReader = PdfFileReader(file)
	count = pdfReader.numPages
	all_page_text = ""
	for i in range(count):
		page = pdfReader.getPage(i)
		all_page_text += page.extractText()
	return all_page_text

def main():
	st.title("File Upload App")
	st.write("Check the Menu bar in the left to upload different type of documents")
	menu=["Images","Dataset","DocumentFiles","Audio","Video","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Images":
		st.subheader("Images")
		image_file = st.file_uploader("Upload Images",
			type=["png","jpg","jpeg"])
		if image_file is not None:
			# To see details
			st.write(type(image_file))
			# Methods/Attrib
			#st.write(dir(image_file))
			file_details = {"filename":image_file.name,
							"filetype":image_file.type,
							"filesize":image_file.size}
			st.write(file_details)
			st.image(load_image(image_file), width=250, height=250)

	elif choice == "Dataset":
		st.subheader("Dataset")
		data_file = st.file_uploader("Upload CSV",type=["csv"])
		if data_file is not None:
			st.write(type(data_file))
			file_details = {"filename":data_file.name,
							"filetype":data_file.type,
							"filesize":data_file.size}
			st.write(file_details)
			df = pd.read_csv(data_file)
			st.dataframe(df)

	elif choice == "DocumentFiles":
		st.subheader("DocumentFiles")
		docx_file = st.file_uploader("Upload Document",type=["pdf","docx","txt"])
		if st.button("Process"):
			if docx_file is not None:
				file_details = {"filename":docx_file.name,
							"filetype":docx_file.type,
							"filesize":docx_file.size}
				st.write(file_details)
				if docx_file.type == "text/plain":
					# Read as bytes
					# raw_text = docx_file.read()
					# st.write(raw_text) # works but in bytes
					# st.text(raw_text) # does work as expected

					# Read as string (decode bytes to string)
					raw_text = str(docx_file.read(),"utf-8")
					st.write(raw_text) # Work
					# st.text(raw_text)  # Work
				elif docx_file.type == "application/pdf":
					# Using PyPDF2
					raw_text = read_pdf(docx_file)
					st.write(raw_text)


					# Using pdfplumber
					# try:
					# 	with pdfplumber.open(docx_file) as pdf:
					# 		pages = pdf.pages[0]
					# 		st.write(pages.extract_text())
					# except:
					# 	st.write("None")

				else:
					raw_text = docx2txt.process(docx_file)
					st.write(raw_text)
					# st.text(raw_text)

	elif choice == "Audio":
		st.subheader("Audio")
		audio_file = st.file_uploader("Upload Audio",
			type=["mp3"])
		if st.button("Process"):
			st.write(type(audio_file))
			file_details = {"filename":audio_file.name,
							"filetype":audio_file.type,
							"filesize":audio_file.size}
			st.write(file_details)
			st.audio(audio_file.read())

	elif choice == 'Video':
		st.subheader("Video")
		video_file = st.file_uploader("Upload Audio",
			type=["mp4"])
		if st.button("Process"):
			st.write(type(video_file))
			file_details = {"filename":video_file.name,
							"filetype":video_file.type,
							"filesize":video_file.size}
			st.write(file_details)
			st.video(video_file, start_time=3)

	else:
		st.subheader("About")
		st.write("This is File Upload Application to upload Images, Audio, Video, Dataset, Document Files.")
		st.write("It converts and process document files such as txt, docx, pdf documents to raw text")
		st.write("by : Allentine Paulis - 2021")





if __name__ == '__main__':
	main()
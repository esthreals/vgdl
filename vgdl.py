import urllib.request
import pyperclip



def pixhost(response):
	image_links = ""

	print("Total images on page:", len(response)-1)

	for i in range(1, len(response)):
		image_link = "https://pixhost.to/show/" + response[i].split("\"")[0]
		request2 = urllib.request.Request(image_link, 
			headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'})
		response2 = str(urllib.request.urlopen(request2).read())
		splitstring = "pixhost.to/images/"
		response2 = response2.split(splitstring)
		image_link_final = response2[len(response2)-2].split("\"")[-1] + "pixhost.to/images/" + response2[-1].split("\"")[0]
		image_links += image_link_final + "\n"
		print("Image", i, "/", len(response)-1, "done, Progress = " + str(round(i/(len(response)-1)*100, 2)) + "%   ", 
			  end='\r')

	print(i, "image links are collected and copied to your clipboard.")
	pyperclip.copy(image_links)
	spam = pyperclip.paste()


def vipr(response):
	image_links = ""

	print("Total images on page:", len(response)-1)

	for i in range(1, len(response)):
		image_link = "https://vipr.im/" + response[i].split("\"")[0]
		request2 = urllib.request.Request(image_link, 
			headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'})
		response2 = str(urllib.request.urlopen(request2).read())
		splitstring = "vipr.im/i/"
		response2 = response2.split(splitstring)
		image_link_final = response2[0].split("\"")[-1] + "vipr.im/i/" + response2[1].split("\"")[0]
		image_links += image_link_final + "\n"
		print("Image", i, "/", len(response)-1, "done, Progress = " + str(round(i/(len(response)-1)*100, 2)) + "%   ", 
			  end='\r')

	print(i, "image links are collected and copied to your clipboard.")
	pyperclip.copy(image_links)
	spam = pyperclip.paste()


def acidimg(response):
	image_links = ""

	print("Total images on page:", len(response)-1)

	for i in range(1, len(response)):
		image_link = "https://acidimg.cc/" + response[i].split("\"")[0]
		data = urllib.parse.urlencode({"imgContinue": "hey"}).encode()
		request2 = urllib.request.Request(image_link, 
			headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'},
			data=data)
		response2 = str(urllib.request.urlopen(request2).read())
		splitstring = "src=\"https://acidimg.cc/"
		response2 = response2.split(splitstring)
		image_link_final = "https://acidimg.cc/" + response2[1].split("\"")[0]
		image_links += image_link_final + "\n"
		print("Image", i, "/", len(response)-1, "done, Progress = " + str(round(i/(len(response)-1)*100, 2)) + "%   ", 
			  end='\r')

	print(i, "image links are collected and copied to your clipboard.")
	pyperclip.copy(image_links)
	spam = pyperclip.paste()


def imx(response):
	image_links = ""

	print("Total images on page:", len(response)-1)

	for i in range(1, len(response)):
		image_link = "https://imx.to/" + response[i].split("\"")[0]
		data = urllib.parse.urlencode({"imgContinue": "hey"}).encode()
		request2 = urllib.request.Request(image_link, 
			headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'},
			data=data)
		response2 = str(urllib.request.urlopen(request2).read())
		splitstring = "src=\"https://imx.to/"
		response2 = response2.split(splitstring)
		image_link_final = "https://imx.to/" + response2[1].split("\"")[0]
		image_links += image_link_final + "\n"
		print("Image", i, "/", len(response)-1, "done, Progress = " + str(round(i/(len(response)-1)*100, 2)) + "%   ", 
			  end='\r')

	print(i, "image links are collected and copied to your clipboard.")
	pyperclip.copy(image_links)
	spam = pyperclip.paste()


def main():
	url = input("Url of the gallery (https://vipergirls.to/threads/1234567-Gallery-Name-):\n")

	request =  urllib.request.Request(url, 
		headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'})
	response = str(urllib.request.urlopen(request).read())	
	

	# Bigger than 10 for stray images hosted by different hosts. 
	if len(response.split("href=\"https://imx.to/")) > 10:
		imx(response.split("href=\"https://imx.to/"))
	elif len(response.split("href=\"https://acidimg.cc/")) > 10:
		acidimg(response.split("href=\"https://acidimg.cc/"))
	elif len(response.split("href=\"https://vipr.im/")) > 10:
		vipr(response.split("href=\"https://vipr.im/"))
	elif len(response.split("href=\"https://pixhost.to/show/")) > 10:
		pixhost(response.split("href=\"https://pixhost.to/show/"))

	print("You can now close this window.")


if __name__ == "__main__":
	main()

from bs4 import BeautifulSoup

with open('index.html', 'r') as f:
    content = f.read()

    soup = BeautifulSoup(content, 'lxml')

    # # grab tag
    # tags = soup.find_all('h1')
    # for tag in tags:
    #     print(tag.text)

    course_cards = soup.find_all('div', class_='card')

    for course in course_cards:
        # h5 stores info about name and a stores price
        course_name = course.h5.text
        # access the last elem
        course_price = course.a.text.split()[-1]

        print(course_name + " costs " + course_price)

        # test

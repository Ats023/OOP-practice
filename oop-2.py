#Bookshop inventory #not complete
class stock:
    stock_pos=0
    def __init__(self, title, author, publisher, price):
        self.title=title
        self.author=author
        self.publisher=publisher
        self.price=price

        stock.stock_pos+=1

        self.pos=stock.stock_pos
    
    @classmethod
    def add_book(cls, book_str):
        title, author, publisher, price=book_str.split('/')
        return cls(title, author, publisher, price)

    def display(self):
        return 'Title: {}\nAuthor: {}\npublisher: {}\nPrice: {}'.format(self.title,self.author,self.publisher,self.price)        

print('Enter books in format: book_id-title/author/publisher/price')
while True:
    x=input('Add book: ')
    if x!='':
        x.split('-')[0]=stock.add_book(x.split('-')[1])
        print(x.split('-')[0].title, 'added')
    else:
        break

print('No. of books: ', stock.stock_pos)



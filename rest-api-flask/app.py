from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data - Assuming this as our database
books = [
    {"id": 1, "title": "Python Programming", "author": "Guido van Rossum"},
    {"id": 2, "title": "Java Programming", "author": "James Gosling"}
]

# Route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({"books": books})

# Route to get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify({"book": book}), 200
    else:
        return jsonify({"message": "Book not found"}), 404

# Route to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = {"id": len(books) + 1, "title": data['title'], "author": data['author']}
    books.append(new_book)
    return jsonify({"message": "Book added successfully", "book": new_book}), 201

# Route to update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        book.update(data)
        return jsonify({"message": "Book updated successfully", "book": book}), 200
    else:
        return jsonify({"message": "Book not found"}), 404

# Route to delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({"message": "Book deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)

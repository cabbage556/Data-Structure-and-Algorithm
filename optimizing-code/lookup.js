const authors = [
    { authorId: 1, name: "Virginia Woolf" },
    { authorId: 2, name: "Leo Tolstoy" },
    { authorId: 3, name: "Dr.Seuss" },
    { authorId: 4, name: "J.K.Rowling" },
    { authorId: 5, name: "Mark Twain" },
];

const books = [
    { authorId: 3, title: "Hop on Pop" },
    { authorId: 1, title: "Mrs.Dalloway" },
    { authorId: 4, title: "Harry Porter and the Sorcerer's Stone" },
    { authorId: 1, title: "To the Lighthouse" },
    { authorId: 2, title: "Anna Karenina" },
    { authorId: 5, title: "The Adventures of Tom Sawyer" },
    { authorId: 3, title: "The Cat in the Hat" },
    { authorId: 2, title: "War and Peace" },
    { authorId: 3, title: "Green Eggs and Ham" },
    { authorId: 5, title: "The Advantures of Huckleberry Finn" },
];

function connectBooksWithAuthors(books, authors) {
    const booksWithAuthors = [];
    const authorHashTable = {};

    // 저자 데이터를 저자 해시 테이블로 변환한다.
    authors.forEach((author) => {
        authorHashTable[author.authorId] = author.name;
    });

    books.forEach((book) => {
        booksWithAuthors.push({
            title: book.title,
            author: authorHashTable[book.authorId],
        });
    });

    return booksWithAuthors;
}

console.log(connectBooksWithAuthors(books, authors));

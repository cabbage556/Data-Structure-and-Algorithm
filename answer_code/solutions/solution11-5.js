/***
 * Excerpted from "A Common-Sense Guide to Data Structures and Algorithms, Second Edition",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/jwdsal2 for more book information.
 ***/
function uniquePaths(rows, columns) {
  if (rows === 1 || columns === 1) {
    return 1;
  }

  return uniquePaths(rows - 1, columns) + uniquePaths(rows, columns - 1);
}

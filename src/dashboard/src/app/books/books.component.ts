import { Component, OnInit } from '@angular/core';
import { BookService } from '../book.service';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-books',
  templateUrl: './books.component.html',
  styleUrls: ['./books.component.css']
})
export class BooksComponent implements OnInit {
  title = new FormControl('');
  author = new FormControl('');
  publicationDate = new FormControl('');

  constructor(private bookService: BookService) { }

  ngOnInit(): void {
  }

  createBook(): void {
    this.bookService.createBook(this.title.value, this.author.value, this.publicationDate.value)
      .subscribe(
        response => {
          console.log('User created successfully:', response);
          // Perform any additional actions after user creation
        },
        error => {
          console.error('Error creating user:', error);
          // Handle error scenarios
        }
      );
  }
}

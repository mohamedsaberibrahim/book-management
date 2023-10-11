import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BookService {
  private apiUrl = 'http://localhost:8000/api/v1/books';

  constructor(private http: HttpClient) { }

  createBook(title: string, author: string, publicationDate: Date): Observable<any> {
    const book = { title, author, publication_date: publicationDate };
    return this.http.post(this.apiUrl, book);
  }
}

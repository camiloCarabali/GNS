import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class APIService {
  readonly endpoint = 'http://127.0.0.1:8000/';

  constructor(private http: HttpClient) {}

  getUserList(): Observable<any[]> {
    return this.http.get<any[]>(this.endpoint + 'showUsers/');
  }

  getPostList(): Observable<any[]> {
    return this.http.get<any[]>(this.endpoint + 'showPosts/');
  }

  getPhotoList(val: any): Observable<any[]> {
    return this.http.get<any[]>(this.endpoint + 'searchPhotosUsers/' + val)
  }

  getRequestList(): Observable<any[]> {
    return this.http.get<any[]>(this.endpoint + 'showRequests')
  }

  updateRequest(val: any){
    return this.http.put(this.endpoint + 'modifyRequests/', val)
  }

  deleteRequest(val: any){
    return this.http.delete(this.endpoint + 'deleteRequests/' + val)
  }

  


}

import { Component, OnInit } from '@angular/core';
import { APIService } from 'src/services/api.service';

@Component({
  selector: 'app-show-photo',
  templateUrl: './show-photo.component.html',
  styleUrls: ['./show-photo.component.sass']
})
export class ShowPhotoComponent implements OnInit {
  p: number = 1;

  constructor(private service: APIService) { }

  PhotoList: any = []

  userId: string = '';

  ngOnInit(): void {
  }

  showPhotosUsersList(){
    var userId = this.userId
    this.service.getPhotoList(userId).subscribe((data)=> {
      this.PhotoList = data
    })
  }

}

import { Component, OnInit } from '@angular/core';
import { APIService } from 'src/services/api.service';

@Component({
  selector: 'app-show-post',
  templateUrl: './show-post.component.html',
  styleUrls: ['./show-post.component.sass'],
})
export class ShowPostComponent implements OnInit {
  p: number = 1;

  constructor(private service: APIService) {}

  PostList: any = [];

  ngOnInit(): void {
    this.showPostList();
  }

  showPostList() {
    this.service.getPostList().subscribe((data) => {
      this.PostList = data;
    });
  }
}

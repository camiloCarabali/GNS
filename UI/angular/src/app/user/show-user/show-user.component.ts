import { Component, OnInit } from '@angular/core';
import { APIService } from 'src/services/api.service';

@Component({
  selector: 'app-show-user',
  templateUrl: './show-user.component.html',
  styleUrls: ['./show-user.component.sass'],
})
export class ShowUserComponent implements OnInit {
  p: number = 1;

  constructor(private service: APIService) {}

  UserList: any = [];

  ngOnInit(): void {
    this.showUserList();
  }

  showUserList() {
    this.service.getUserList().subscribe((data) => {
      this.UserList = data;
    });
  }
}

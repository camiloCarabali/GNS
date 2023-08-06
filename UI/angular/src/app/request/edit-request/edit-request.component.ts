import { Component, OnInit, Input } from '@angular/core';
import { APIService } from 'src/services/api.service';

@Component({
  selector: 'app-edit-request',
  templateUrl: './edit-request.component.html',
  styleUrls: ['./edit-request.component.sass'],
})
export class EditRequestComponent implements OnInit {
  constructor(private service: APIService) {}

  @Input() req: any;
  id: string = '';
  date: any;
  method: string = '';
  consult: string = '';
  dataReturn: string = '';

  ngOnInit(): void {
    this.id = this.req.id;
    this.date = this.req.date;
    this.method = this.req.method;
    this.consult = this.req.consult;
    this.dataReturn = this.req.dataReturn;
  }

  updateRequest() {
    var val = {
      id: this.id,
      date: this.date,
      method: this.method,
      consult: this.consult,
      dataReturn: this.dataReturn,
    };

    this.service.updateRequest(val).subscribe((res) => {
      alert(res.toString());
    });
  }
}

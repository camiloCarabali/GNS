import { Component, OnInit } from '@angular/core';
import { APIService } from 'src/services/api.service';
import * as XLSX from 'xlsx';

@Component({
  selector: 'app-show-request',
  templateUrl: './show-request.component.html',
  styleUrls: ['./show-request.component.sass'],
})
export class ShowRequestComponent implements OnInit {
  p: number = 1;

  expandedItemIndex = -1;

  constructor(private service: APIService) {}

  requestList: any = [];
  requestListComplete: any = [];

  ModalTitle: string = '';
  activateEditComp: boolean = false;
  req: any;

  ngOnInit(): void {
    this.showRequestList();
  }

  closeClick() {
    this.activateEditComp = false;
    this.showRequestList();
  }

  showRequestList() {
    this.service.getRequestList().subscribe((data) => {
      this.requestListComplete = JSON.parse(JSON.stringify(data));
      this.requestList = data;
    });
  }

  editRequest(item: any) {
    this.req = item;
    this.ModalTitle = 'Edit Request';
    this.activateEditComp = true;
  }

  toggleExpanded(index: number) {
    if (this.expandedItemIndex === index) {
      this.expandedItemIndex = -1;
    } else {
      this.expandedItemIndex = index;
    }
  }

  exportToExcel() {
    const dataToExport = JSON.parse(JSON.stringify(this.requestListComplete));
    const headers = Object.keys(dataToExport[0]);
    const rows = dataToExport.map((obj: any) => Object.values(obj));

    rows.unshift(headers);

    const worksheet: XLSX.WorkSheet = XLSX.utils.aoa_to_sheet(rows);
    const workbook: XLSX.WorkBook = XLSX.utils.book_new();

    XLSX.utils.book_append_sheet(workbook, worksheet, 'Datos');

    const excelBuffer: any = XLSX.write(workbook, {
      bookType: 'xlsx',
      type: 'array',
    });
    const blob = new Blob([excelBuffer], {
      type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    });
    const fileName = 'data.xlsx';

    const url = window.URL.createObjectURL(blob);
    const anchor = document.createElement('a');
    anchor.href = url;
    anchor.download = fileName;
    anchor.click();
    window.URL.revokeObjectURL(url);
  }

  deleteRequest(item: any) {
    if (confirm('Are you Sure?')) {
      this.service.deleteRequest(item.id).subscribe((data) => {
        alert(data.toString());
        this.showRequestList();
      });
    }
  }
}

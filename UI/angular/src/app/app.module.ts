import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { UserComponent } from './user/user.component';
import { ShowUserComponent } from './user/show-user/show-user.component';
import { PostComponent } from './post/post.component';
import { ShowPostComponent } from './post/show-post/show-post.component';
import { APIService } from 'src/services/api.service';
import { HttpClientModule } from '@angular/common/http';
import { NgxPaginationModule } from 'ngx-pagination';
import { PhotoComponent } from './photo/photo.component';
import { ShowPhotoComponent } from './photo/show-photo/show-photo.component';
import { FormsModule } from '@angular/forms';
import { RequestComponent } from './request/request.component';
import { ShowRequestComponent } from './request/show-request/show-request.component';
import { EditRequestComponent } from './request/edit-request/edit-request.component';

@NgModule({
  declarations: [
    AppComponent,
    UserComponent,
    ShowUserComponent,
    PostComponent,
    ShowPostComponent,
    PhotoComponent,
    ShowPhotoComponent,
    RequestComponent,
    ShowRequestComponent,
    EditRequestComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    NgxPaginationModule,
    FormsModule,
  ],
  providers: [APIService],
  bootstrap: [AppComponent],
})
export class AppModule {}

import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UserComponent } from './user/user.component';
import { PostComponent } from './post/post.component';
import { PhotoComponent } from './photo/photo.component';
import { RequestComponent } from './request/request.component';

const routes: Routes = [
  { path: 'user', component: UserComponent },
  { path: 'post', component: PostComponent },
  { path: 'photo', component: PhotoComponent },
  { path: 'request', component: RequestComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}

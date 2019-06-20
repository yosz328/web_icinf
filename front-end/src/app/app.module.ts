import { RouterModule, Routes } from '@angular/router';

import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CabeceraComponent } from './cabecera/cabecera.component';
import { RedesSocialesComponent } from './redes-sociales/redes-sociales.component';
import { PerfilComponent } from './perfil/perfil.component';
import { NoticiasComponent } from './noticias/noticias.component';
import { MaterialapoyoComponent } from './materialapoyo/materialapoyo.component';
import { ProfesoresComponent } from './profesores/profesores.component';
import { ContactoComponent } from './contacto/contacto.component';
import { InicioComponent } from './inicio/inicio.component';

	


const routes: Routes = [
  { path: 'noticias', component: NoticiasComponent },
  { path: 'publica', component: PerfilComponent },
  { path: 'profesores', component: ProfesoresComponent },
  { path: 'contacto', component: ContactoComponent },
  { path: 'materialapoyo', component: MaterialapoyoComponent },
  { path: '', component: InicioComponent, pathMatch: 'full' },
  { path: '**', redirectTo: '/', pathMatch: 'full' },
];

@NgModule({
  declarations: [
    AppComponent,
    CabeceraComponent,
    RedesSocialesComponent,
    PerfilComponent,
    NoticiasComponent,
    MaterialapoyoComponent,
    ProfesoresComponent,
    ContactoComponent,
	InicioComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule, 
    RouterModule.forRoot(routes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

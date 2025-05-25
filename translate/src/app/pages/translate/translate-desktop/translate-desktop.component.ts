import {Component, inject, OnInit} from '@angular/core';
import {Store} from '@ngxs/store';
import {takeUntil, tap} from 'rxjs/operators';
import {BaseComponent} from '../../../components/base/base.component';
import {IonButton, IonButtons, IonContent, IonHeader, IonTitle, IonToolbar} from '@ionic/angular/standalone';
import {TranslateInputButtonComponent} from '../input/button/button.component';
import {LanguageSelectorsComponent} from '../language-selectors/language-selectors.component';
import {TranslocoPipe} from '@jsverse/transloco';
import {NtkmeButtonModule} from '@ctrl/ngx-github-buttons';
import {SpokenToSignedComponent} from '../spoken-to-signed/spoken-to-signed.component';

import {DropPoseFileComponent} from '../drop-pose-file/drop-pose-file.component';
import {addIcons} from 'ionicons';
import {cloudUpload, language, videocam} from 'ionicons/icons';
import {RouterLink} from '@angular/router';
import { IonicModule } from '@ionic/angular';
import { CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';

@Component({
  selector: 'app-translate-desktop',
  templateUrl: './translate-desktop.component.html',
  styleUrls: ['./translate-desktop.component.scss'],
  imports: [
    //IonHeader,
    //IonToolbar,
    //IonButtons,
    //IonContent,
    //IonTitle,
    TranslateInputButtonComponent,
    LanguageSelectorsComponent,
    //TranslocoPipe,
    SpokenToSignedComponent,
    //SignedToSpokenComponent,
    DropPoseFileComponent,
    //IonButton,
   // RouterLink,
    IonicModule,
   
    
  ],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class TranslateDesktopComponent extends BaseComponent implements OnInit {
  private store = inject(Store);
  spokenToSigned$ = this.store.select<boolean>(state => state.translate.spokenToSigned);

  spokenToSigned: boolean;

  constructor() {
    super();

    addIcons({language, videocam, cloudUpload});
  }

  

  ngOnInit(): void {
    this.spokenToSigned$
      .pipe(
        tap(spokenToSigned => (this.spokenToSigned = spokenToSigned)),
        takeUntil(this.ngUnsubscribe)
      )
      .subscribe();
  }

  goBack(): void {
    window.location.href = 'http://127.0.0.1:8000/animation/';
  }
}

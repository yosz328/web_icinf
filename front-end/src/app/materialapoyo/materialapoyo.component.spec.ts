import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MaterialapoyoComponent } from './materialapoyo.component';

describe('MaterialapoyoComponent', () => {
  let component: MaterialapoyoComponent;
  let fixture: ComponentFixture<MaterialapoyoComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MaterialapoyoComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MaterialapoyoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

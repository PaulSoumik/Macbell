import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  templateUrl: './profile.component.html',
  styleUrls: ['./user-model.component.css']
})
export class ProfileComponent implements OnInit {

    name = 'abc xyz';
    mobile = "2385075847";
    email = "seriuvyi@shenrh";
    id = "iweu";
    category = "intern";
    firm_name = "-";

  constructor(
    private router : Router
  ) { }

  ngOnInit(): void {
    /* get details and update em */

  }

  onSubmit() {
    console.log("Update Profile");
    this.router.navigate(['/updateProfile']);
  }

}

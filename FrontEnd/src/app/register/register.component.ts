import { Component, OnInit } from '@angular/core';
// import { Router, ActivatedRoute } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';


@Component({
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  form: FormGroup;
    loading = false;
    submitted = false;
    step1 = true;
    step2 = false;
    profileTypes = {
        'student': ['intership', 'job seeker', 'freelancing work', 'startup idea', 'startup', 'join startup as a cofounder', 'join startup as team member'],
        'entrepreneur': ['startup idea', 'startup', 'join startup as a cofounder', 'join startup as team member'],
        'student entrepreneur': ['intership', 'job seeker', 'freelancing work', 'startup idea', 'startup', 'join startup as a cofounder', 'join startup as team member'],
        'businessman': ['company', 'firm' , 'franchisee' , 'Distributors', 'wholesalers' , 'investor'],
        'investor' : ['investor'],
        'freelancer' : ['freelancer']
    };
    profiles = [];

    constructor(
        private formBuilder: FormBuilder,
        private http: HttpClient
    ) { }

    ngOnInit() {
        // console.log(this.profileTypes.keys());
        console.log(typeof(this.profileTypes));
        this.form = this.formBuilder.group({
            firstName: ['', Validators.required],
            lastName: ['', Validators.required],
            email: ['', Validators.required],
            password: ['', [Validators.required, Validators.minLength(6)]],
            category: ['', [Validators.required]],
            profileType: ['', [Validators.required]],
            // address: ['', [Validators.required]],
            // contact: ['', [Validators.required, Validators.minLength(9)]],
            // country: ['', [Validators.required]],
            // city: ['', [Validators.required]],
        });
    }

    // convenience getter for easy access to form fields
    get f() { return this.form.controls; }

    changeProfileType (val) {
        this.profiles = this.profileTypes[val];
    }

    onSubmit() {
        this.submitted = true;
        // this.form.reset();
        

        if (this.form.invalid) {
            console.log("form invalid");
            return;
        }
        else {
            console.log(this.form.value)

            this.http.post<any>('url', {
                email: this.form.value.email,
                password: this.form.value.password,
                name: this.form.value.firstName + this.form.value.lastName,
                category: this.form.value.category,
                profileType: this.form.value.profileType
            }).subscribe({
                next: data => console.log(data),
                error: error => console.error(error, "Error during register")
            });

        }
        
        // this.loading = true;
    }

}

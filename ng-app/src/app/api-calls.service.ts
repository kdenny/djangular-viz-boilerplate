import { Injectable } from '@angular/core';
import {Http, Response, Headers, RequestOptions} from "@angular/http";

import 'rxjs/add/operator/toPromise';

@Injectable()
export class ApiCallsService {

  private apiUrl;
  exampleResult;

  constructor(private http: Http) {
    this.apiUrl = 'http://127.0.0.1:8007/';
  }

  getResult() {

    let resultUrl = this.apiUrl + 'results';

    let headers = new Headers({ 'Content-Type': 'application/json'});

    let options = new RequestOptions({ headers: headers });
    return this.http.get(resultUrl, options).toPromise()
      .then(response => response.json())
	}

}

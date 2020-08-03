package com.example.krishimoney.ui;

import android.app.ProgressDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.text.Editable;
import android.util.Log;
import android.view.View;
import android.webkit.WebView;
import android.widget.ArrayAdapter;
import android.widget.AutoCompleteTextView;
import android.widget.Button;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.VolleyLog;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;
import com.example.krishimoney.R;
import com.google.android.material.textfield.TextInputLayout;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import org.json.JSONException;
import org.json.JSONObject;
import org.json.JSONArray;

import java.lang.reflect.Type;
import java.text.NumberFormat;
import java.util.HashMap;
import java.util.List;
import java.util.Locale;

public class Crop_Arrival extends AppCompatActivity {

        private static final String[] item = new String[]{"Onion","Tomato","Cotton","Jowar","Rice","Tur","Coffee","Garlic","Lemon","Sugarcane"};
        TextInputLayout textlayOut;
        RequestQueue requestQueue;
    private WebView webView;
        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_crop__arrival);
            AutoCompleteTextView act1 = (AutoCompleteTextView)findViewById(R.id.dropdown_text) ;
            textlayOut = findViewById(R.id.text_input_layout);
            ArrayAdapter<String> adapter = new ArrayAdapter<String>(this,android.R.layout.simple_dropdown_item_1line,item);
            act1.setAdapter(adapter);

            ((Button) findViewById(R.id.btnSubmit)).setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    openPriceActivity();
                }
            });
        }

    public void openPriceActivity(){
        requestQueue = Volley.newRequestQueue(this);
        callPreFunc();
    }

    private void callPreFunc()
    {
        final ProgressDialog progress = new ProgressDialog(this);
        progress.setMessage("Please wait...");
        progress.setCancelable(false); // disable dismiss by tapping outside of the dialog
        progress.show();

        final String URL = "http://192.168.43.131:8026/cropArrival";
        // Post params to be sent to the server
        HashMap<String, String> params = new HashMap<String, String>();
        final String str = textlayOut.getEditText().getText().toString();
        params.put("commodity", str);

        final JsonObjectRequest req = new JsonObjectRequest(URL, new JSONObject(params),
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        try {
                            VolleyLog.v("Response:%n %s", response.toString(4));
                            Log.d("myTag", response.toString(4));
                            JSONObject jsonObj = new JSONObject(response.toString());
                            JSONArray prediction = jsonObj.getJSONArray("prediction");

                            String webString = "<html>\n" +
                                    "<body>\n" +
                                    "\n" +
                                    "<h2>Crop :" +  str + "</h2>\n" +
                                    "\n" +
                                    "<table border=1 width=80%>\n" +
                                    "  <tr>\n" +
                                    "    <th>Date</th>\n" +
                                    "    <th>Arrival (Unit Quintal)</th> \n" +
                                    "  </tr>\n";

                            for (int i = 0; i < prediction.length(); i++) {
                                JSONObject c = prediction.getJSONObject(i);

                                String arrival = c.getString("Arrival (unit quintal)");
                                double value = Double.parseDouble(arrival);
                                String strVal =  String.format("%.2f", value);
                                String date = c.getString("Date");

                                webString = webString + "<tr><td>" + date + "</td><td>" + strVal + "</td></tr>";

                            }

                            webString = webString + "</table>\n" +
                                    "\n" +
                                    "</body>\n" +
                                    "</html>";
                            webView = (WebView) findViewById(R.id.webview1);
                            webView.getSettings().setJavaScriptEnabled(true);
                            webView.loadData(webString, "text/html; charset=utf-8", "UTF-8");
                            //webView.loadUrl(myIntent.getStringExtra("strUrl"));
                            webView.setVerticalScrollBarEnabled(true);
                            webView.setHorizontalScrollBarEnabled(true);
                            progress.dismiss();
                        } catch (JSONException e) {
                            progress.dismiss();
                            e.printStackTrace();
                            showAlertMessage("Some error occurred!, Please try after sometime");
                        }
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                progress.dismiss();
                showAlertMessage("Some error occurred!, Please try after sometime");
                VolleyLog.e("Error1: ", error.getMessage());
                if (error == null || error.networkResponse == null) {
                    return;
                }
            }
        });
        req.setRetryPolicy(new DefaultRetryPolicy(
                50000,
                DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));
        requestQueue.add(req);
    }

    private void showAlertMessage(String message)
    {
        AlertDialog.Builder builder1 = new AlertDialog.Builder(this);
        builder1.setMessage(message);
        builder1.setCancelable(true);

        /*builder1.setPositiveButton(
                "Yes",
                new DialogInterface.OnClickListener() {
                    public void onClick(DialogInterface dialog, int id) {
                        dialog.cancel();
                    }
                });*/

        builder1.setNegativeButton(
                "OK",
                new DialogInterface.OnClickListener() {
                    public void onClick(DialogInterface dialog, int id) {
                        dialog.cancel();
                    }
                });

        AlertDialog alert11 = builder1.create();
        alert11.show();
    }


    }

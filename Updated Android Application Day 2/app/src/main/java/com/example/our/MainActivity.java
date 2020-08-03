package com.example.our;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import android.Manifest;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.basgeekball.awesomevalidation.AwesomeValidation;
import com.basgeekball.awesomevalidation.ValidationStyle;
import com.basgeekball.awesomevalidation.utility.RegexTemplate;

import java.io.File;

public class MainActivity extends AppCompatActivity {

    EditText etName,etMobile,etPassword,etConfirmPassword;
    Button btSubmit;
    AwesomeValidation awesomeValidation;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        etName =findViewById(R.id.et_name);
        etMobile =findViewById(R.id.et_mobile);
        etPassword =findViewById(R.id.et_password);
        etConfirmPassword =findViewById(R.id.et_confirm_password);
        btSubmit =findViewById(R.id.bt_submit);

        awesomeValidation =new AwesomeValidation(ValidationStyle.BASIC);

        awesomeValidation.addValidation(this,R.id.et_name,
                RegexTemplate.NOT_EMPTY,R.string.invalid_name);

         //awesomeValidation.addValidation(this,R.id.et_mobile,
               // "[5-9] {1} [0-9] {9}$",R.string.invalid_mobile);

        awesomeValidation.addValidation(this,R.id.et_password,
                ".{4,}",R.string.invalid_password);

        awesomeValidation.addValidation(this,R.id.et_confirm_password,
                R.id.et_password,R.string.invalid_confirm_password);



        btSubmit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(awesomeValidation.validate()){
                    Toast.makeText(getApplicationContext(),"Validate Successfully",Toast.LENGTH_SHORT).show();
                    btSubmit.setOnClickListener(new View.OnClickListener(){
                        public void onClick(View v){
                            startActivity(new Intent(getApplicationContext(), price_prediction.class));
                        }
                    });
                    if(ContextCompat.checkSelfPermission(MainActivity.this, Manifest.permission.WRITE_EXTERNAL_STORAGE)!= PackageManager.PERMISSION_GRANTED){
                        ActivityCompat.requestPermissions(MainActivity.this,new String[]{Manifest.permission.WRITE_EXTERNAL_STORAGE},0);
                    }

                    else{
                        String name1= etName.getText().toString();
                        String mob1= etMobile.getText().toString();
                        String pass1= etPassword.getText().toString();

                        File file= new  File("/Desktop/file.csv");
                        file.mkdir();

                        String csv="/Desktop/file.csv";

                    }
                }
                else {
                    Toast.makeText(getApplicationContext(),"Validation Failed",Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}
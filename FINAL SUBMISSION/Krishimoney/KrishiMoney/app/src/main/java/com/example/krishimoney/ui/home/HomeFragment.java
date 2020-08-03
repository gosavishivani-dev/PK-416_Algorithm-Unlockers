package com.example.krishimoney.ui.home;

import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.Observer;
import androidx.lifecycle.ViewModelProviders;

import com.example.krishimoney.R;
import com.example.krishimoney.ui.Crop_Arrival;
import com.example.krishimoney.ui.Other;
import com.example.krishimoney.ui.Predict_Price;
import com.example.krishimoney.ui.Predict_Psf;


public class HomeFragment extends Fragment {

    private HomeViewModel homeViewModel;

    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        homeViewModel =
                ViewModelProviders.of(this).get(HomeViewModel.class);
        View root = inflater.inflate(R.layout.fragment_home, container, false);
        final TextView textView = root.findViewById(R.id.text_home);
        homeViewModel.getText().observe(getViewLifecycleOwner(), new Observer<String>() {
            @Override
            public void onChanged(@Nullable String s) {
                textView.setText(s);
            }
        });
        ((Button) root.findViewById(R.id.btn_Crop_Arrival)).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openCropArrival();
            }
        });
        ((Button) root.findViewById(R.id.btn_Price_Prediction)).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openCropPrice();
            }
        });
        ((Button) root.findViewById(R.id.btn_Todays_Price)).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openCropPSF();
            }
        });
        ((Button) root.findViewById(R.id.btn_Other)).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openTemp();
            }
        });
        return root;
    }

    public void openCropArrival(){
        Intent intent = new Intent(getActivity(), Crop_Arrival.class);
        startActivity(intent);
    }

    public void openCropPrice(){
        Intent intent = new Intent(getActivity(), Predict_Price.class);
        startActivity(intent);
    }

    public void openCropPSF(){
        Intent intent = new Intent(getActivity(), Predict_Psf.class);
        startActivity(intent);
    }

    public void openTemp(){
        Intent intent = new Intent(getActivity(), Other.class);
        startActivity(intent);
    }
}
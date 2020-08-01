package com.example.krishimoney.ui;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

import java.util.List;

public class PredictPrice {

@SerializedName("error")
@Expose
private String error;
@SerializedName("message")
@Expose
private String message;

    @Override
    public String toString() {
        return "PredictPrice{" +
                "error='" + error + '\'' +
                ", message='" + message + '\'' +
                ", prediction=" + prediction +
                '}';
    }

    @SerializedName("prediction")
@Expose
private Prediction prediction;

public String getError() {
return error;
}

public void setError(String error) {
this.error = error;
}

public String getMessage() {
return message;
}

public void setMessage(String message) {
this.message = message;
}

public Prediction getPrediction() {
return prediction;
}

public void setPrediction(Prediction prediction) {
this.prediction = prediction;
}




    public class Prediction {

        @SerializedName("Arrival (unit quintal)")
        @Expose
        private String arrivalUnitQuintal;
        @SerializedName("Commodity")
        @Expose
        private String commodity;
        @SerializedName("Date")
        @Expose
        private String date;

        public String getArrivalUnitQuintal() {
            return arrivalUnitQuintal;
        }

        public void setArrivalUnitQuintal(String arrivalUnitQuintal) {
            this.arrivalUnitQuintal = arrivalUnitQuintal;
        }

        public String getCommodity() {
            return commodity;
        }

        public void setCommodity(String commodity) {
            this.commodity = commodity;
        }

        public String getDate() {
            return date;
        }

        public void setDate(String date) {
            this.date = date;
        }
    }
}


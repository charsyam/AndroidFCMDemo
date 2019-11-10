package win.hawin.fcmdemo;

import android.content.Context;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import java.util.HashMap;
import java.util.Map;

public class NetUtils {
    public static void sendTokenToServer(Context context, final String token) {
        RequestQueue queue = Volley.newRequestQueue(context);
        String url = "https://nadia003.hawin.win/api/register";

        // Request a string response from the provided URL.
        StringRequest stringRequest = new StringRequest(Request.Method.POST, url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        // Display the first 500 characters of the response string.
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
            }
        }) {
            protected Map<String, String> getParams()
            {
                Map<String, String> params = new HashMap<String, String>();
                params.put("userid", "charsyam");
                params.put("token", token);

                return params;
            }};

        // Add the request to the RequestQueue.
        queue.add(stringRequest);
    }

}

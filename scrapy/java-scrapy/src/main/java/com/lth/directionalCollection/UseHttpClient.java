package com.lth.directionalCollection;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.util.EntityUtils;

import java.io.IOException;

/**
 * Created by lth on 17-4-26.
 */
public class UseHttpClient {
    public String downloadPage(String path) throws IOException {
        CloseableHttpClient httpClient = HttpClientBuilder.create().build();
        HttpGet httpGet = new HttpGet(path);
        HttpResponse response = httpClient.execute(httpGet);

        HttpEntity entity = response.getEntity();
        if (entity != null) {
            String html = EntityUtils.toString(entity, "GBK");
            EntityUtils.consume(entity);
            return html;
        }
        return null;
    }

    public String downHtml(String url) throws IOException {
        String content = null;

        DefaultHttpClient httpClient = new DefaultHttpClient();
        HttpGet httpGet = new HttpGet(url);
        HttpResponse response = httpClient.execute(httpGet);

        HttpEntity entity = response.getEntity();
        if (entity != null) {
            content = EntityUtils.toString(entity, "utf-8");
            EntityUtils.consume(entity);
        }

        httpClient.getConnectionManager().shutdown();
        return content;
    }


}

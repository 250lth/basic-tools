package com.lth.directionalCollection;

import java.io.*;
import java.net.Socket;
import java.net.URL;
import java.net.URLConnection;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

/**
 * Created by lth on 17-4-26.
 */
public class RetrivePage {
    /**
     * Use java.net.URL to construct url
     */
    public static String downloadPage(String path) throws IOException {
        URL pageURL = new URL(path);
        BufferedReader reader = new BufferedReader(new InputStreamReader(pageURL.openStream()));
        String line;
        StringBuilder pageBuffer = new StringBuilder();
        while ((line = reader.readLine()) != null)
            pageBuffer.append(line);
        return pageBuffer.toString();
    }

    public String useScanner(String path) throws IOException {
        URL pageURL = new URL(path);
        Scanner scanner = new Scanner(new InputStreamReader(pageURL.openStream(), "utf-8"));
        scanner.useDelimiter("\\z");
        StringBuilder pageBuffer = new StringBuilder();
        while (scanner.hasNext())
            pageBuffer.append(scanner.next());
        return pageBuffer.toString();
    }

    public void useSocket() throws IOException {
        String host = "nba.hupu.com";
        String file = "/index.html";
        int port = 80;

        Socket s = new Socket(host, port);

        OutputStream out = s.getOutputStream();
        PrintWriter outw = new PrintWriter(out, false);
        outw.println("GET " + file + " HTTP/1.0\r\n");
        outw.println("Accept: text/plain, text/html, text/*\r\n");
        outw.println("\r\n");
        outw.flush();

        InputStream in = s.getInputStream();
        InputStreamReader inr = new InputStreamReader(in);
        BufferedReader br = new BufferedReader(inr);
        String line;
        while ((line = br.readLine()) != null)
            System.out.println(line);
    }

    public String getHeaderField(String fieldKey) throws IOException {
        String path = "http://bbs.hupu.com";
        URL url = new URL(path);
        URLConnection con = url.openConnection();
        Map<String, List<String>> header = con.getHeaderFields();

        Iterator i = header.keySet().iterator();
        String key = null;
        while (i.hasNext()) {
            key = (String)i.next();
            if (key == null) {
                if (fieldKey == null)
                    return (String)((List)(header.get(null))).get(0);
                else {
                    if (key.equalsIgnoreCase(fieldKey))
                        return (String)(header.get(key)).get(0);
                }
            }
        }
        return null;
    }

    public static void main(String[] args) throws IOException {
        System.out.println(RetrivePage.downloadPage("http://nba.hupu.com"));
    }
}

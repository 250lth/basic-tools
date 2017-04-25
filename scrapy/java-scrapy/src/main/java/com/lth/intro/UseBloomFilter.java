package com.lth.intro;

/**
 * Created by lth on 17-4-25.
 */
public class UseBloomFilter {
    public static void main(String[] args) {
        BloomFilter<String> urlSeen = new BloomFilter<String>(100, 4);
        urlSeen.add("bbs.hupu.com");
        urlSeen.add("www.sina.com");
        urlSeen.add("www.qq.com");
        urlSeen.add("www.sohu.com");

        if (urlSeen.contains("bbs.hupu.com")) {
            System.out.println("已经存在的概率是：" +
                    (1 - urlSeen.expectedFalsePositiveProbability()));
        } else {
            System.out.println("一定不存在！！！");
        }
    }
}

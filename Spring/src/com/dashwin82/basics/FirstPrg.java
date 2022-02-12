package com.dashwin82.basics;

import org.springframework.beans.factory.BeanFactory;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.Resource;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.springframework.context.ConfigurableApplicationContext;

public class FirstPrg {

    public static void main(String[] args) {

    /* via Bean Factory
    Resource resource = new ClassPathResource("applicationContext.xml");
    @SuppressWarnings("deprecation")
    BeanFactory factory = new XmlBeanFactory(resource);

     */

    //ApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
        ConfigurableApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");

        // Student student = (Student) factory.getBean("studentbean");
        Student student = (Student) context.getBean("studentbean");
        System.out.println("Fetched from bean: " + student.getName());

        context.registerShutdownHook();
    }
}

package com.dashwin82.annotations;

import java.lang.annotation.ElementType;
import java.lang.annotation.Target;

//using target annotation to annotate a type
@Target(ElementType.TYPE_USE)
// Declaring a simple type annotation
@interface TypeAnnoDemo{}

public class TypeAnnotation {

    public static void main(String[] args)
    {
        //Annotating the type of String
        @TypeAnnoDemo String str = "I am annotated with type annotation";
        System.out.println(str);
        funcRetAnnotation();
    }

    static @TypeAnnoDemo int funcRetAnnotation()
    {
        System.out.println("this is function return type annotation");
        return 0;
    }
}

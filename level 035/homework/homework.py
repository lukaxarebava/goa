def manual_join(separator, elements):  
     if not elements:
         return ""
    
     result = ""
     for i, element in enumerate(elements):
         result += str(element)
         if i < len(elements) - 1:
             result += separator
     return result

my_list = ["apple", "banana", "cherry"]
result = manual_join(", ", my_list)
print(result) 
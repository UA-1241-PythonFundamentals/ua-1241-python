def reverse(st):
    split_text = st.split()
    
    reverse_text = split_text[::-1]
    
    return " ".join(reverse_text)
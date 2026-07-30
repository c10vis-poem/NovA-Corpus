My bad. Here is exactly what the file looks like, with no extra fluff.

Create a file named **SKILL.md** and paste this text inside it:

> ---  
> name: text-summarizer  
> description: Use when the user asks to summarize, condense, or
> bullet-point long text or files.  
> version: 1.0.0  
> ---  
>   
> \# Text Summarizer Skill  
>   
> 1. Read the text provided by the user.  
> 2. Extract the top 3 most important takeaways.  
> 3. Output the result in this exact format:  
>   
> \### 📌 Summary  
> \[Insert a 2-sentence high-level overview here\]  
>   
> \### 🔑 Key Takeaways  
> \* \[Takeaway 1\]  
> \* \[Takeaway 2\]  
> \* \[Takeaway 3\]

To use it in your chat, you just type:

/text-summarizer \[your text here\]

Would you like me to make a quick template for a **different specific
task**, or does this structure make sense now?

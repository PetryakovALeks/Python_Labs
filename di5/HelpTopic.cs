﻿public class HelpTopic
{
    public string Title { get; set; }
    public string Content { get; set; }

    public override string ToString()
    {
        return Title;
    }
}

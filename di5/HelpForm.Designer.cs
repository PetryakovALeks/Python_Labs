namespace di5
{
    partial class HelpForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.txtSearch = new System.Windows.Forms.TextBox();
            this.lstTopics = new System.Windows.Forms.ListBox();
            this.rtbHelpText = new System.Windows.Forms.RichTextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // txtSearch
            // 
            this.txtSearch.BackColor = System.Drawing.SystemColors.Info;
            this.txtSearch.Location = new System.Drawing.Point(104, 28);
            this.txtSearch.Name = "txtSearch";
            this.txtSearch.Size = new System.Drawing.Size(684, 22);
            this.txtSearch.TabIndex = 0;
            this.txtSearch.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            // 
            // lstTopics
            // 
            this.lstTopics.BackColor = System.Drawing.SystemColors.Info;
            this.lstTopics.FormattingEnabled = true;
            this.lstTopics.ItemHeight = 16;
            this.lstTopics.Location = new System.Drawing.Point(25, 80);
            this.lstTopics.Name = "lstTopics";
            this.lstTopics.Size = new System.Drawing.Size(347, 324);
            this.lstTopics.TabIndex = 1;
            this.lstTopics.SelectedIndexChanged += new System.EventHandler(this.lstTopics_SelectedIndexChanged);
            // 
            // rtbHelpText
            // 
            this.rtbHelpText.BackColor = System.Drawing.SystemColors.Info;
            this.rtbHelpText.Location = new System.Drawing.Point(443, 80);
            this.rtbHelpText.Name = "rtbHelpText";
            this.rtbHelpText.Size = new System.Drawing.Size(334, 324);
            this.rtbHelpText.TabIndex = 2;
            this.rtbHelpText.Text = "";
            this.rtbHelpText.TextChanged += new System.EventHandler(this.rtbHelpText_TextChanged);
            // 
            // button1
            // 
            this.button1.BackColor = System.Drawing.Color.Red;
            this.button1.Location = new System.Drawing.Point(12, 27);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 3;
            this.button1.Text = "Назад";
            this.button1.UseVisualStyleBackColor = false;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // HelpForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImage = global::di5.Properties.Resources._5;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.rtbHelpText);
            this.Controls.Add(this.lstTopics);
            this.Controls.Add(this.txtSearch);
            this.Name = "HelpForm";
            this.Text = "HelpForm";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox txtSearch;
        private System.Windows.Forms.ListBox lstTopics;
        private System.Windows.Forms.RichTextBox rtbHelpText;
        private System.Windows.Forms.Button button1;
    }
}
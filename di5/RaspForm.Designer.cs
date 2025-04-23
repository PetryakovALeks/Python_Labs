namespace di5
{
    partial class RaspForm
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
            this.back_but1 = new System.Windows.Forms.Button();
            this.home_but = new System.Windows.Forms.Button();
            this.away_but = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // back_but1
            // 
            this.back_but1.BackColor = System.Drawing.Color.Red;
            this.back_but1.Location = new System.Drawing.Point(12, 12);
            this.back_but1.Name = "back_but1";
            this.back_but1.Size = new System.Drawing.Size(177, 23);
            this.back_but1.TabIndex = 0;
            this.back_but1.Text = "НА главную";
            this.back_but1.UseVisualStyleBackColor = false;
            this.back_but1.Click += new System.EventHandler(this.back_but1_Click);
            // 
            // home_but
            // 
            this.home_but.BackColor = System.Drawing.Color.Salmon;
            this.home_but.Location = new System.Drawing.Point(59, 533);
            this.home_but.Name = "home_but";
            this.home_but.Size = new System.Drawing.Size(308, 98);
            this.home_but.TabIndex = 1;
            this.home_but.Text = "Домашние";
            this.home_but.UseVisualStyleBackColor = false;
            this.home_but.Click += new System.EventHandler(this.home_but_Click);
            // 
            // away_but
            // 
            this.away_but.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(128)))), ((int)(((byte)(128)))), ((int)(((byte)(255)))));
            this.away_but.Location = new System.Drawing.Point(1038, 545);
            this.away_but.Name = "away_but";
            this.away_but.Size = new System.Drawing.Size(308, 98);
            this.away_but.TabIndex = 2;
            this.away_but.Text = "Гостевые матчи";
            this.away_but.UseVisualStyleBackColor = false;
            this.away_but.Click += new System.EventHandler(this.away_but_Click);
            // 
            // RaspForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImage = global::di5.Properties.Resources._4;
            this.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.ClientSize = new System.Drawing.Size(1482, 753);
            this.Controls.Add(this.away_but);
            this.Controls.Add(this.home_but);
            this.Controls.Add(this.back_but1);
            this.Name = "RaspForm";
            this.Text = "RaspForm";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button back_but1;
        private System.Windows.Forms.Button home_but;
        private System.Windows.Forms.Button away_but;
    }
}
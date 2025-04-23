namespace di5
{
    partial class ButTicketForm
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
            this.Vip_But = new System.Windows.Forms.Button();
            this.sec_but = new System.Windows.Forms.Button();
            this.third_but = new System.Windows.Forms.Button();
            this.first_but = new System.Windows.Forms.Button();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // Vip_But
            // 
            this.Vip_But.BackColor = System.Drawing.Color.Yellow;
            this.Vip_But.Location = new System.Drawing.Point(844, 418);
            this.Vip_But.Name = "Vip_But";
            this.Vip_But.Size = new System.Drawing.Size(163, 62);
            this.Vip_But.TabIndex = 0;
            this.Vip_But.Text = "Vip";
            this.Vip_But.UseVisualStyleBackColor = false;
            this.Vip_But.Click += new System.EventHandler(this.Vip_But_Click);
            // 
            // sec_but
            // 
            this.sec_but.BackColor = System.Drawing.Color.Red;
            this.sec_but.Location = new System.Drawing.Point(844, 504);
            this.sec_but.Name = "sec_but";
            this.sec_but.Size = new System.Drawing.Size(163, 62);
            this.sec_but.TabIndex = 1;
            this.sec_but.Text = "2-категория";
            this.sec_but.UseVisualStyleBackColor = false;
            this.sec_but.Click += new System.EventHandler(this.sec_but_Click);
            // 
            // third_but
            // 
            this.third_but.BackColor = System.Drawing.Color.Lime;
            this.third_but.Location = new System.Drawing.Point(1067, 504);
            this.third_but.Name = "third_but";
            this.third_but.Size = new System.Drawing.Size(163, 62);
            this.third_but.TabIndex = 2;
            this.third_but.Text = "3 категория";
            this.third_but.UseVisualStyleBackColor = false;
            this.third_but.Click += new System.EventHandler(this.third_but_Click);
            // 
            // first_but
            // 
            this.first_but.BackColor = System.Drawing.Color.Blue;
            this.first_but.Location = new System.Drawing.Point(1067, 418);
            this.first_but.Name = "first_but";
            this.first_but.Size = new System.Drawing.Size(163, 62);
            this.first_but.TabIndex = 3;
            this.first_but.Text = "1 категория";
            this.first_but.UseVisualStyleBackColor = false;
            this.first_but.Click += new System.EventHandler(this.first_but_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Image = global::di5.Properties.Resources._1;
            this.pictureBox1.Location = new System.Drawing.Point(732, 66);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(604, 290);
            this.pictureBox1.TabIndex = 4;
            this.pictureBox1.TabStop = false;
            // 
            // ButTicketForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImage = global::di5.Properties.Resources._2;
            this.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.ClientSize = new System.Drawing.Size(1482, 753);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.first_but);
            this.Controls.Add(this.third_but);
            this.Controls.Add(this.sec_but);
            this.Controls.Add(this.Vip_But);
            this.Name = "ButTicketForm";
            this.Text = "ButTicketForm";
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button Vip_But;
        private System.Windows.Forms.Button sec_but;
        private System.Windows.Forms.Button third_but;
        private System.Windows.Forms.Button first_but;
        private System.Windows.Forms.PictureBox pictureBox1;
    }
}
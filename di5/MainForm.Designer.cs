namespace di5
{
    partial class MainForm
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.rasp_but = new System.Windows.Forms.Button();
            this.team_but = new System.Windows.Forms.Button();
            this.my_but = new System.Windows.Forms.Button();
            this.history_bat = new System.Windows.Forms.Button();
            this.Admin_but = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // rasp_but
            // 
            this.rasp_but.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(128)))), ((int)(((byte)(128)))), ((int)(((byte)(255)))));
            this.rasp_but.Location = new System.Drawing.Point(31, 332);
            this.rasp_but.Name = "rasp_but";
            this.rasp_but.Size = new System.Drawing.Size(174, 60);
            this.rasp_but.TabIndex = 0;
            this.rasp_but.Text = "Матчи";
            this.rasp_but.UseVisualStyleBackColor = false;
            this.rasp_but.Click += new System.EventHandler(this.rasp_but_Click);
            // 
            // team_but
            // 
            this.team_but.BackColor = System.Drawing.Color.Salmon;
            this.team_but.Location = new System.Drawing.Point(270, 332);
            this.team_but.Name = "team_but";
            this.team_but.Size = new System.Drawing.Size(174, 60);
            this.team_but.TabIndex = 1;
            this.team_but.Text = "Состав";
            this.team_but.UseVisualStyleBackColor = false;
            this.team_but.Click += new System.EventHandler(this.team_but_Click);
            // 
            // my_but
            // 
            this.my_but.BackColor = System.Drawing.Color.Salmon;
            this.my_but.Location = new System.Drawing.Point(725, 332);
            this.my_but.Name = "my_but";
            this.my_but.Size = new System.Drawing.Size(174, 60);
            this.my_but.TabIndex = 3;
            this.my_but.Text = "Мои билеты";
            this.my_but.UseVisualStyleBackColor = false;
            this.my_but.Click += new System.EventHandler(this.my_but_Click);
            // 
            // history_bat
            // 
            this.history_bat.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(128)))), ((int)(((byte)(128)))), ((int)(((byte)(255)))));
            this.history_bat.Location = new System.Drawing.Point(509, 332);
            this.history_bat.Name = "history_bat";
            this.history_bat.Size = new System.Drawing.Size(174, 60);
            this.history_bat.TabIndex = 2;
            this.history_bat.Text = "История";
            this.history_bat.UseVisualStyleBackColor = false;
            this.history_bat.Click += new System.EventHandler(this.history_bat_Click);
            // 
            // Admin_but
            // 
            this.Admin_but.BackColor = System.Drawing.Color.Yellow;
            this.Admin_but.Location = new System.Drawing.Point(12, 12);
            this.Admin_but.Name = "Admin_but";
            this.Admin_but.Size = new System.Drawing.Size(130, 23);
            this.Admin_but.TabIndex = 4;
            this.Admin_but.Text = "Редактировать";
            this.Admin_but.UseVisualStyleBackColor = false;
            this.Admin_but.Click += new System.EventHandler(this.Admin_but_Click);
            // 
            // button1
            // 
            this.button1.BackColor = System.Drawing.SystemColors.Info;
            this.button1.Location = new System.Drawing.Point(882, 12);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 5;
            this.button1.Text = "Справка";
            this.button1.UseVisualStyleBackColor = false;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImage = global::di5.Properties.Resources._5;
            this.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.ClientSize = new System.Drawing.Size(982, 413);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.Admin_but);
            this.Controls.Add(this.my_but);
            this.Controls.Add(this.history_bat);
            this.Controls.Add(this.team_but);
            this.Controls.Add(this.rasp_but);
            this.Name = "MainForm";
            this.Text = "Form1";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button rasp_but;
        private System.Windows.Forms.Button team_but;
        private System.Windows.Forms.Button history_bat;
        private System.Windows.Forms.Button my_but;
        private System.Windows.Forms.Button Admin_but;
        private System.Windows.Forms.Button button1;
    }
}


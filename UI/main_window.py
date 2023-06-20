import tkinter as tk
if __name__ == '__main__':
    window = tk.Tk()

    # Create frames
    frm_settings = tk.Frame(bg="green")
    frm_results = tk.Frame(bg="red")

    # Create left frame components
    lbl_settings_title = tk.Label(text="Settings", master=frm_settings)
    lbl_settings_title.pack()
    btn_run_alg = tk.Button(text="Run", master=frm_settings)
    btn_run_alg.pack()

    # Create right frame components
    lbl_results_title = tk.Label(text="Results", master=frm_results)
    lbl_results_title.pack()

    # Pack frames
    frm_settings.pack(side=tk.LEFT, fill=tk.Y)
    frm_results.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    window.mainloop()

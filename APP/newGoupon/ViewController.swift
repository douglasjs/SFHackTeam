//
//  ViewController.swift
//  newGoupon
//
//  Created by TakFai Chan on 02/03/2019.
//  Copyright © 2019 TakFai Chan. All rights reserved.
//

import UIKit
import SCSDKLoginKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    
    @IBAction func showMessage(sender: UIButton) {
        
        
        let _ = SCSDKLoginButton() {(success : Bool, error : Error?) in
            
            let alertController = UIAlertController(title: "The first one", message: "Login Ok",   preferredStyle: .alert)
            alertController.addAction(UIAlertAction(title: "OK", style: .destructive, handler: nil))
            self.present(alertController, animated: true, completion: nil)
            
        }
        
        
        
     
    }
    
    

    
  

}


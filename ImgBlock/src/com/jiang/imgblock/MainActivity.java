package com.jiang.imgblock;

import android.app.Activity;
import android.os.Bundle;

public class MainActivity extends Activity {
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		
		this.mView = new GameView(this);
		this.setContentView(this.mView);
		super.onCreate(savedInstanceState);
	}
	
	private GameView mView;

}

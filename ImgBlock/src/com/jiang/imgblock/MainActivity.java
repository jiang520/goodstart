package com.jiang.imgblock;

import java.util.Random;

import android.app.Activity;
import android.app.Notification.Action;
import android.content.Intent;
import android.media.audiofx.AudioEffect.OnControlStatusChangeListener;
import android.os.Bundle;
import android.view.ContextMenu;
import android.view.KeyEvent;
import android.view.Menu;
import android.view.MenuItem;
import android.view.MotionEvent;
import android.view.View;
import android.view.Window;
import android.view.ContextMenu.ContextMenuInfo;
import android.view.View.OnCreateContextMenuListener;

public class MainActivity extends Activity {
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		
		this.requestWindowFeature(Window.FEATURE_NO_TITLE);
		this.mView = new GameView(this);
		this.setContentView(this.mView);
		super.onCreate(savedInstanceState);
	}
	
	@Override
	public boolean onTouchEvent(MotionEvent event) {
		// TODO Auto-generated method stub
		if(event.getAction()==MotionEvent.ACTION_DOWN)
		{
			this.mView.touchAt(event.getX(),event.getY());
		}
		return super.onTouchEvent(event);
	}
	
	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// TODO Auto-generated method stub
		menu.add(1, 0, 0, "Restart");
		menu.add(1, 1, 0, "Change level");
		menu.add(1, 2, 0, "Change img");
		menu.add(1, 3, 0, "Quit");
		
		return super.onCreateOptionsMenu(menu);
	}
	@Override  
	 public boolean onKeyDown(int keyCode, KeyEvent event) {  
	  if (keyCode == KeyEvent.KEYCODE_BACK && event.getRepeatCount() == 1) { // 按下的如果是BACK，同时没有重复  
	   Intent home = new Intent(Intent.ACTION_MAIN);  
	   home.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);  
	   home.addCategory(Intent.CATEGORY_HOME);  
	   startActivity(home);  
	  }  
	  return super.onKeyDown(keyCode, event);  
	 }  
	@Override
	public boolean onOptionsItemSelected(MenuItem item) {
		// TODO Auto-generated method stub
		switch(item.getItemId())
		{
		case 0:{//restart
			this.mView.restart();
			this.mView.invalidate();
			break;
		}
		case 1:{//change level
			for(;;)
			{
				int nLevel = Math.abs(new Random().nextInt())%4+3;
				if(nLevel!=this.mView.GetLevel()) 
				{
					this.mView.setLevel(nLevel);
					this.mView.invalidate();
					break;
				}
			}
			break;
		}			
		case 2:{//change image			
				int ids[]={
						R.drawable.img0,
						R.drawable.img1,
						R.drawable.img2,
						R.drawable.img3,
				};
				int nid = Math.abs(new Random().nextInt())%4;
				this.mView.setImage(ids[nid]);
				this.mView.invalidate();
				break;
			}
		case 3:{//quit
			System.exit(0);
			break;
		}			
		}
		return super.onOptionsItemSelected(item);
	}
	private GameView mView;

}

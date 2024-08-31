package thisisthepy.pycomposeui

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.InlineTextContent
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.runtime.MutableState
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.text.AnnotatedString
import androidx.compose.ui.text.TextLayoutResult
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontStyle
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.text.style.TextDecoration
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.TextUnit
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp


@JvmName("SimpleIcon")
@Composable
fun IconWrapper(
    icon: ImageVector,
    contentDescription: String,
    modifier: Modifier,
    color: Long
) {
    Icons.Default.Favorite
    Icon(icon, contentDescription, modifier, Color(color))
}


val FavoriteIcon
    @JvmName("FavoriteIcon")
    get() = Icons.Default.Favorite


val AddIcon
    @JvmName("AddIcon")
    get() = Icons.Default.Add


val KeyboardArrowDownIcon
    @JvmName("KeyboardArrowDownIcon")
    get() = Icons.Default.KeyboardArrowDown


val KeyboardArrowUpIcon
    @JvmName("KeyboardArrowUpIcon")
    get() = Icons.Default.KeyboardArrowUp


val PlayArrowIcon
    @JvmName("PlayArrowIcon")
    get() = Icons.Default.PlayArrow


val DeleteIcon
    @JvmName("DeleteIcon")
    get() = Icons.Default.Delete



@JvmName("SimpleTextWidget")
@Composable
fun SimpleTextWidget(
    text: String,
    color: Long,
    fontSize: Float
) {
    Text(text, Modifier, Color(color), fontSize.sp)
}


@JvmName("SimpleSpacer")
@Composable
fun SimpleSpacer(
    start: Float, top: Float, end: Float, bottom: Float
) {
    Spacer(Modifier.padding(start.dp, top.dp, end.dp, bottom.dp))
}


@JvmName("TextWidget")
@Composable
fun TextWidget(
    text: String,
    modifier: Modifier = Modifier,
    color: Color = Color.Unspecified,
    fontSize: TextUnit = TextUnit.Unspecified,
    fontStyle: FontStyle? = null,
    fontWeight: FontWeight? = null,
    fontFamily: FontFamily? = null,
    letterSpacing: TextUnit = TextUnit.Unspecified,
    textDecoration: TextDecoration? = null,
    textAlign: TextAlign? = null,
    lineHeight: TextUnit = TextUnit.Unspecified,
    overflow: TextOverflow = TextOverflow.Clip,
    softWrap: Boolean = true,
    maxLines: Int = Int.MAX_VALUE,
    minLines: Int = 1,
    onTextLayout: (TextLayoutResult) -> Unit = {},
    style: TextStyle = LocalTextStyle.current
) {
    Text(text, modifier, color, fontSize, fontStyle, fontWeight, fontFamily, letterSpacing, textDecoration, textAlign,
        lineHeight, overflow, softWrap, maxLines, minLines, onTextLayout, style)
}


@JvmName("AnnotatedStringTextWidget")
@Composable
fun AnnotatedStringTextWidget(
    text: AnnotatedString,
    modifier: Modifier = Modifier,
    color: Color = Color.Unspecified,
    fontSize: TextUnit = TextUnit.Unspecified,
    fontStyle: FontStyle? = null,
    fontWeight: FontWeight? = null,
    fontFamily: FontFamily? = null,
    letterSpacing: TextUnit = TextUnit.Unspecified,
    textDecoration: TextDecoration? = null,
    textAlign: TextAlign? = null,
    lineHeight: TextUnit = TextUnit.Unspecified,
    overflow: TextOverflow = TextOverflow.Clip,
    softWrap: Boolean = true,
    maxLines: Int = Int.MAX_VALUE,
    minLines: Int = 1,
    inlineContent: Map<String, InlineTextContent> = mapOf(),
    onTextLayout: (TextLayoutResult) -> Unit = {},
    style: TextStyle = LocalTextStyle.current
) {
    Text(text, modifier, color, fontSize, fontStyle, fontWeight, fontFamily, letterSpacing, textDecoration, textAlign,
        lineHeight, overflow, softWrap, maxLines, minLines, inlineContent, onTextLayout, style)
}

@JvmName("SimpleColumnWidget")
@Composable
fun SimpleColumnWidget(
    modifier: Modifier,
    verticalArrangement: Arrangement.Vertical,
    horizontalAlignment: Alignment.Horizontal,
    content: () -> Unit
) {
    Column(modifier, verticalArrangement, horizontalAlignment) {
        content()
    }
}


@JvmName("SimpleRowWidget")
@Composable
fun SimpleRowWidget(
    modifier: Modifier,
    horizontalArrangement: Arrangement.Horizontal,
    verticalAlignment: Alignment.Vertical,
    content: () -> Unit
) {
    Row(modifier, horizontalArrangement, verticalAlignment) {
        content()
    }
}


@JvmName("SimpleButtonWidget")
@Composable
fun SimpleButtonWidget(
    onClick: () -> Unit,
    enabled: Boolean,
    cornerRadius: Float,
    color: Long,
    content: () -> Unit
) {
    Button(onClick, Modifier, enabled, RoundedCornerShape(cornerRadius.dp), ButtonColors(
        containerColor = Color(color),
        contentColor = Color.Unspecified,
        disabledContainerColor = Color(color),
        disabledContentColor = Color.Unspecified
    )
    ) {
        content()
    }
}


@JvmName("SimpleCardWidget")
@Composable
fun SimpleCardWidget(
    cornerRadius: Float,
    color: Long,
    content: () -> Unit
) {
    Card(Modifier, RoundedCornerShape(cornerRadius.dp), CardColors(
        containerColor = Color(color),
        contentColor = Color.Unspecified,
        disabledContainerColor = Color(color),
        disabledContentColor = Color.Unspecified
    )
    ){
        content()
    }
}


@JvmName("SimpleTextField")
@Composable
fun SimpleTextField(
    textState: MutableState<String>,
    padding: Int
) {
    TextField(
        value = textState.value, // 외부에서 받은 텍스트 상태 사용
        onValueChange = { textState.value = it }, // 텍스트 값이 변경될 때 호출되는 콜백
        placeholder = null, // placeholder 생략
        modifier = Modifier
            .fillMaxWidth()
            .padding(padding.dp),
        singleLine = false
    )
}
